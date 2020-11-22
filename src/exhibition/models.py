from django.db import models
from django.db.models.deletion import DO_NOTHING, SET_NULL
from django.db.models.expressions import F
from django.template.defaultfilters import default

from client.models import artist, client

# Create your models here.


class exhibtion(models.Model):
    name = models.CharField(max_length=32, blank=False)
    is_active = models.BooleanField(default=False)
    exhibition_day = models.DateField(blank=False)
    exhibition_location = models.CharField(blank=False, max_length=32)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}-{self.date_created.strftime('%d-%m-%Y')}"


class art(models.Model):
    exhibtion = models.ForeignKey(exhibtion, on_delete=models.CASCADE)
    artist = models.ForeignKey(artist, on_delete=models.CASCADE)
    minimum_price = models.DecimalField(max_digits=20, decimal_places=2)
    name = models.CharField(max_length=32, blank=False)
    photo = models.ImageField(default="profile.png",
                              upload_to='exibition/photo/')
    video = models.FileField(upload_to="exibition/videos")
    description = models.CharField(max_length=200, blank=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name}-{self.date_created.strftime('%d-%m-%Y')}"


class auction(models.Model):
    art = models.ForeignKey(art, on_delete=models.CASCADE)
    client = models.ForeignKey(client, on_delete=models.CASCADE)
    bid_amount = models.DecimalField(max_digits=20, decimal_places=2)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.client.user.username}-{self.bid_amount}"
