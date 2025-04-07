from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from django.utils.timezone import now
from mainapp.models import Ticket

import json

from mainapp.models import Event, Team, Stadium, Ticket
import qrcode
from io import BytesIO
from django.http import HttpResponse
from mainapp.models import Ticket


# 🔹 Liste des matchs
def list_events(request):
    events = Event.objects.select_related('stadium', 'team_home', 'team_away').all()
    events_data = [{
        'id': event.id,
        'stadium': str(event.stadium),
        'home_team': str(event.team_home) if event.team_home else None,
        'away_team': str(event.team_away) if event.team_away else None,
        'start': event.start,
        'score': event.score
    } for event in events]
    return JsonResponse(events_data, safe=False)


# 🔹 Liste des équipes
def list_teams(request):
    teams = Team.objects.all()
    teams_data = [{
        'id': team.id,
        'name': team.name,
        'code': team.code,
        'nickname': team.nickname,
        'flag': team.flag
    } for team in teams]
    return JsonResponse(teams_data, safe=False)


# 🔹 Liste des stades
def list_stadiums(request):
    stadiums = Stadium.objects.all()
    stadiums_data = [{
        'id': stadium.id,
        'name': stadium.name,
        'location': stadium.location
    } for stadium in stadiums]
    return JsonResponse(stadiums_data, safe=False)


# 🔹 Connexion utilisateur
@csrf_exempt
@require_http_methods(["POST"])
def user_login(request):
    try:
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')

        print("Tentative de login :")
        print("Username :", username)
        print("Password :", password)

        user = authenticate(request, username=username, password=password)
        print("Résultat de authenticate() :", user)

        if user is not None:
            login(request, user)
            return JsonResponse({
                'status': 'success',
                'message': 'Logged in successfully',
                'user': {
                    'id': user.id,
                    'username': user.username,
                    'email': user.email
                }
            })
        else:
            return JsonResponse({
                'status': 'error',
                'message': 'Invalid credentials'
            }, status=401)

    except json.JSONDecodeError:
        return JsonResponse({'status': 'error', 'message': 'Invalid JSON'}, status=400)


# 🔹 Création d'utilisateur
@csrf_exempt
@require_http_methods(["POST"])
def user_register(request):
    try:
        data = json.loads(request.body)
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')

        if not username or not email or not password:
            return JsonResponse({'status': 'error', 'message': 'Tous les champs sont obligatoires'}, status=400)

        if User.objects.filter(username=username).exists():
            return JsonResponse({'status': 'error', 'message': 'Nom d’utilisateur déjà pris'}, status=400)

        user = User.objects.create_user(username=username, email=email, password=password)

        return JsonResponse({
            'status': 'success',
            'message': 'Utilisateur enregistré avec succès',
            'user': {
                'id': user.id,
                'username': user.username,
                'email': user.email
            }
        })

    except IntegrityError:
        return JsonResponse({'status': 'error', 'message': 'Erreur à l’enregistrement'}, status=400)
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=500)


# 🔹 Déconnexion
def user_logout(request):
    logout(request)
    return JsonResponse({'status': 'success', 'message': 'Déconnexion réussie'})


# 🔹 Vérification connexion
def check_auth(request):
    if request.user.is_authenticated:
        return JsonResponse({'status': 'authenticated'})
    return JsonResponse({'status': 'not_authenticated'}, status=401)


# 🔹 Détail d’un match
def get_event_details(request, event_id):
    try:
        event = Event.objects.select_related('stadium', 'team_home', 'team_away').get(id=event_id)
        return JsonResponse({
            'id': event.id,
            'start': event.start,
            'stadium_id': event.stadium.id if event.stadium else None,
            'stadium': str(event.stadium) if event.stadium else None,
            'team_home_id': event.team_home.id if event.team_home else None,
            'home_team': str(event.team_home) if event.team_home else None,
            'team_away_id': event.team_away.id if event.team_away else None,
            'away_team': str(event.team_away) if event.team_away else None,
        })
    except Event.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'Événement non trouvé'}, status=404)


# 🔹 Mise à jour d’un match (admin)
@csrf_exempt
@login_required
@require_http_methods(["POST"])
def update_event(request, event_id):
    try:
        data = json.loads(request.body)
        event = Event.objects.get(id=event_id)

        if 'start' in data:
            event.start = data['start']
        if 'stadium_id' in data:
            event.stadium_id = data['stadium_id']
        if 'team_home_id' in data:
            event.team_home_id = data['team_home_id']
        if 'team_away_id' in data:
            event.team_away_id = data['team_away_id']

        event.save()

        return JsonResponse({
            'status': 'success',
            'message': 'Événement mis à jour',
            'event_id': event.id
        })
    except Event.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'Événement non trouvé'}, status=404)
    except json.JSONDecodeError:
        return JsonResponse({'status': 'error', 'message': 'Données invalides'}, status=400)


# 🔹 Achat de ticket
@csrf_exempt
@login_required
@require_http_methods(["POST"])
def create_ticket(request):
    try:
        data = json.loads(request.body)
        category = data.get("category")
        event_id = data.get("event_id")

        if not category or not event_id:
            return JsonResponse({"status": "error", "message": "Champs manquants"}, status=400)

        if category not in dict(Ticket.CATEGORY_CHOICES).keys():
            return JsonResponse({"status": "error", "message": "Catégorie invalide"}, status=400)

        try:
            event = Event.objects.get(id=event_id)
        except Event.DoesNotExist:
            return JsonResponse({"status": "error", "message": "Match introuvable"}, status=404)

        ticket = Ticket.objects.create(
            user=request.user.username,
            event=event,
            category=category,
            price=Ticket.PRICES[category],
            purchased_at=now()
        )

        return JsonResponse({
            "status": "success",
            "ticket_id": str(ticket.id),
            "category": ticket.category,
            "price": ticket.price,
            "event": str(ticket.event)
        })

    except json.JSONDecodeError:
        return JsonResponse({"status": "error", "message": "Requête JSON invalide"}, status=400)
    


@csrf_exempt
@login_required
@require_http_methods(["GET"])
def list_user_tickets(request):
    tickets = Ticket.objects.filter(user=request.user.username).select_related('event')
    
    grouped = {}
    for ticket in tickets:
        match = str(ticket.event)
        if match not in grouped:
            grouped[match] = []
        grouped[match].append({
            "ticket_id": str(ticket.id),
            "category": ticket.category,
            "price": ticket.price,
            "purchased_at": ticket.purchased_at
        })

    return JsonResponse({
        "status": "success",
        "tickets": grouped
    })

csrf_exempt
@login_required
@require_http_methods(["GET"])
def generate_qr_code(request, ticket_id):
    try:
        ticket = Ticket.objects.get(id=ticket_id, user=request.user.username)
    except Ticket.DoesNotExist:
        return JsonResponse({"status": "error", "message": "Ticket introuvable ou non autorisé"}, status=404)

    # Génère le QR Code avec l'UUID
    qr = qrcode.make(str(ticket.id))
    buffer = BytesIO()
    qr.save(buffer, format='PNG')
    buffer.seek(0)

    return HttpResponse(buffer, content_type='image/png')

@csrf_exempt
@login_required
@require_http_methods(["DELETE"])
def cancel_ticket(request, ticket_id):
    from mainapp.models import Ticket

    try:
        ticket = Ticket.objects.get(id=ticket_id, user=request.user.username)
        ticket.delete()
        return JsonResponse({"status": "success", "message": "Ticket annulé et remboursé."})
    except Ticket.DoesNotExist:
        return JsonResponse({"status": "error", "message": "Ticket introuvable ou non autorisé."}, status=404)
@csrf_exempt
@require_http_methods(["POST"])
def validate_ticket(request, ticket_id):
    try:
        ticket = Ticket.objects.get(id=ticket_id)
        return JsonResponse({
            "status": "success",
            "message": "Ticket valide",
            "user": ticket.user,
            "category": ticket.category,
            "event": str(ticket.event)
        })
    except Ticket.DoesNotExist:
        return JsonResponse({
            "status": "error",
            "message": "Ticket invalide"
        }, status=404)
