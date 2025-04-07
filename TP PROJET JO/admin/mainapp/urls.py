from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from django.shortcuts import render
from .models import Event
from .views import api

def edit_event(request, event_id):
    event = Event.objects.get(id=event_id)
    return render(request, 'edit_event.html', {'event': event})

urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('admin/login/', TemplateView.as_view(template_name='admin_login.html'), name='admin_login'),
    path('admin/dashboard/', TemplateView.as_view(template_name='admin_dashboard.html'), name='admin_dashboard'),
    path('admin/event/edit/<int:event_id>/', edit_event, name='edit_event'),

    # Admin Django original
    path('django-admin/', admin.site.urls),

    # API Endpoints
    path('api/events/', api.list_events, name='list_events'),
    path('api/events/<int:event_id>/', api.get_event_details, name='event_details'),
    path('api/events/<int:event_id>/update/', api.update_event, name='update_event'),
    path('api/teams/', api.list_teams, name='list_teams'),
    path('api/stadiums/', api.list_stadiums, name='list_stadiums'),
    path('api/check-auth/', api.check_auth, name='check_auth'),
    
    # Authentication
    path('api/login/', api.user_login, name='login'),
    path('api/register/', api.user_register, name='register'),
    path('api/logout/', api.user_logout, name='logout'),

    # Achat de ticket
    path('api/tickets/', api.create_ticket, name='create_ticket'),
    path('api/my-tickets/', api.list_user_tickets, name='list_user_tickets'),

    # Annuler un ticket dans ces billets 
    path('api/tickets/<uuid:ticket_id>/cancel/', api.cancel_ticket, name='cancel_ticket'),


    # Création des qrcodes
    path('api/tickets/<uuid:ticket_id>/qrcode/', api.generate_qr_code, name='generate_qr_code'),

    #verifier si les billets sont valides
    path('api/tickets/<uuid:ticket_id>/validate/', api.validate_ticket, name='validate_ticket'),




]
