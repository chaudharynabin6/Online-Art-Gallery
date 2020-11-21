from django.db import models
from django.db.models.deletion import DO_NOTHING, SET_NULL
from django.db.models.expressions import F
from django.template.defaultfilters import default

from client.models import artist, client

# Create your models here.


class exhibtion(models.Model):
    name = models.CharField(max_length=32, blank=False)
    exhibtion_day = models.DateField(blank=False)
    exhibtion_location = models.CharField(blank=False, max_length=32)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)


class art(models.Model):
    exhibtion = models.OneToOneField(exhibtion, on_delete=DO_NOTHING)
    artist = models.OneToOneField(artist, on_delete=DO_NOTHING)
    minimum_price = models.DecimalField(max_digits=20, decimal_places=2)
    name = models.CharField(max_length=32, blank=False)
    photo = models.ImageField(default="profile.png",
                              upload_to='exibition/photo/')
    video = models.FileField(upload_to="exibition/videos")
    description = models.CharField(max_length=200, blank=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)


class auction(models.Model):
    art = models.OneToOneField(art, on_delete=DO_NOTHING)
    client = models.OneToOneField(client, on_delete=DO_NOTHING)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
