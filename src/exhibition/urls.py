from os import name
from django.urls import path

from artGallery.models import art
from exhibition.models import auction
from .views import exhibition_hall, add_art, art_showcase, approve_art, auction, add_exhibition, manage_exhibition, activate_exhibition, deactivate_exhibition
app_name = "exhibition"
urlpatterns = [
    path("", exhibition_hall, name="exhibition-hall"),
    path("add-art", add_art, name="add-art"),
    path("art-showcase/<int:art_id>", art_showcase, name="art-showcase"),
    path("approve-art", approve_art, name="approve-art"),
    path("auction", auction, name="auction"),
    path("add-exhibition", add_exhibition, name="add-exhibition"),
    path("manage-exhibition", manage_exhibition, name="manage-exhibition"),
    path("activate-exhibition", activate_exhibition, name="activate-exhibition"),
    path("deactivate-exhibition", deactivate_exhibition,
         name="deactivate-exhibition")
]
