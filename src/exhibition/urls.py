from os import name
from django.urls import path

from artGallery.models import art
from .views import exhibition_hall, add_art, art_showcase
app_name = "exhibition"
urlpatterns = [
    path("", exhibition_hall, name="exhibition-hall"),
    path("add-art", add_art, name="add-art"),
    path("art-showcase", art_showcase, name="art-showcase")

]
