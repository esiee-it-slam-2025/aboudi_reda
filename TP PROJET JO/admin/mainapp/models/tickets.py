from django.db import models
from uuid import uuid4
from .event import Event

class Ticket(models.Model):
    CATEGORY_CHOICES = [
        ('Silver', 'Silver'),
        ('Gold', 'Gold'),
        ('Platinum', 'Platinum'),
    ]

    PRICES = {
        'Silver': 100,
        'Gold': 200,
        'Platinum': 300
    }

    id = models.UUIDField(
        primary_key=True, 
        default=uuid4, 
        editable=False
    )
    
    user = models.CharField(
        max_length=100,
        verbose_name="Propriétaire"
    )
    
    event = models.ForeignKey(
        Event, 
        on_delete=models.CASCADE, 
        related_name='tickets',
        verbose_name="Match"
    )
    
    category = models.CharField(
        max_length=20, 
        choices=CATEGORY_CHOICES,
        verbose_name="Catégorie"
    )
    
    price = models.PositiveIntegerField(
        verbose_name="Prix"
    )
    
    purchased_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Date d'achat"
    )

    def save(self, *args, **kwargs):
        if not self.price:
            self.price = self.PRICES[self.category]
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Ticket {self.event} - {self.category} - {self.user}"

    class Meta:
        verbose_name = "Ticket"
        verbose_name_plural = "Tickets"