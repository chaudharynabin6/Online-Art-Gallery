from django.db import models
from artGallery.models import art

# Create your models here.


class cart(models.Model):
    arts = models.ManyToManyField(art, related_name="cart_art")
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.date_created.strftime('%d-%m-%y')}"
