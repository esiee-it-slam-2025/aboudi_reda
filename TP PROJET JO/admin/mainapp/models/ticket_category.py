from django.db import models

class TicketCategory(models.Model):
    CATEGORIES = [
        ('SILVER', 'Silver'),
        ('GOLD', 'Gold'),
        ('PLATINUM', 'Platinum')
    ]

    name = models.CharField(max_length=10, choices=CATEGORIES, unique=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"{self.name} - {self.price}€"