import json
from datetime import datetime
import os
import qrcode
from PIL import Image, ImageDraw, ImageFont

# Lecture des fichiers JSON
stadiums_data = json.load(open('/Users/redaaboudi/Documents/BtsReda/aboudi_reda/TP JO/stadiums.json','r',encoding="utf-8"))

with open('events.json', 'r') as file:
    events_data = json.load(file)

with open('tickets.json', 'r') as file:
    tickets_data = json.load(file)

# satde par id 
stadiums_by_id = {stadium['id']: stadium for stadium in stadiums_data}

# Organiser les données des événements par ID
events_by_id = {event['id']: event for event in events_data}

# Fonction pour formater les dates et heures
def format_datetime(datetime_str):
    dt = datetime.fromisoformat(datetime_str)
    return dt.strftime('%d/%m/%Y'), dt.strftime('%H:%M')

# sauvergade les billets
output_folder = 'tickets'
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# pos x, y du texte
positions = {
    "QR Code": (126, 835),
    "Équipe domicile": (37, 426),
    "Équipe extérieur": (112, 503),
    "Nom du stade + ville": (60, 588),
    "Date & heure de début du match": (60, 656),
    "Catégorie": (20, 756),
    "Place": (200, 756), 
    "Prix du billets": (325,756),
}

# Fonte
font_path = 'Paris2024.ttf'

font36 = ImageFont.truetype('/Users/redaaboudi/Documents/BtsReda/aboudi_reda/TP JO/Paris2024.ttf',36,encoding="utf-8")

# Couleurs
color_blue = (51, 19, 104)
color_white = 'white'

# Tailles de police
font_size_team = 36
font_size_text = 22

# Boucler sur chaque billet
for ticket in tickets_data:
    # Récupérer les informations de l'événement associé
    event = events_by_id.get(ticket['event_id'])
    if event:
        stadium = stadiums_by_id.get(event['stadium_id'])
        if stadium:
            # Créer l'image de fond du billet
            background_img = Image.open('ticketJO.png')
            draw = ImageDraw.Draw(background_img)
            
            # Écrire les informations sur le billet
            draw.text(positions["Équipe domicile"], event['team_home'], fill=color_blue, font=font36)
            draw.text(positions["Équipe extérieur"], event['team_away'], fill=color_blue, font=font36)
            draw.text(positions["Nom du stade + ville"], f"{stadium['name']} - {stadium['location']}", fill=color_white, font=font36)
            draw.text(positions["Date & heure de début du match"], format_datetime(event['start'])[0] + " " + format_datetime(event['start'])[1], fill=color_white, font=font36)
            draw.text(positions["Catégorie"], ticket['category'], fill=color_white, font=font36)
            draw.text(positions["Place"], ticket['seat'] if ticket['seat'] != 'free' else 'Libre', fill=color_white, font=font36)
            draw.text(positions["Prix du billet"], f"{ticket['price']} {ticket['currency']}", fill=color_white, font=font36)
            
            # Générer et placer le QR Code
            qr = qrcode.QRCode(box_size=4)
            qr.add_data(ticket['id'])
            qr_img = qr.make_image(fill_color="black", back_color="white")
            background_img.paste(qr_img, positions["QR Code"])
            
            # Enregistrer le billet
            output_path = os.path.join(output_folder, f"{ticket['id']}_ticket.png")
            background_img.save(output_path)

