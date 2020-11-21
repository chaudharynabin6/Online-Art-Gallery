from os import name
from django.urls import path

from artGallery.models import art
from exhibition.models import auction
from .views import exhibition_hall, add_art, art_showcase, approve_art, auction
app_name = "exhibition"
urlpatterns = [
    path("", exhibition_hall, name="exhibition-hall"),
    path("add-art", add_art, name="add-art"),
    path("art-showcase/<int:art_id>", art_showcase, name="art-showcase"),
    path("approve-art", approve_art, name="approve-art"),
    path("auction", auction, name="auction")
]
