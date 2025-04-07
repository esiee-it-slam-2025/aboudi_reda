from django.contrib import admin
from .models import Event, Stadium, Team, TicketCategory, Ticket

admin.site.register(Event)
admin.site.register(Stadium)
admin.site.register(Team)
admin.site.register(TicketCategory)
admin.site.register(Ticket)