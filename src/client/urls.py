from django.urls import path
from .views import dashboard, update_client_or_artist, add_art
app_name = "client"
urlpatterns = [
    path("", dashboard, name="dashboard"),
    path("client-update", update_client_or_artist, name="client-update"),
    path("add-art", add_art, name="add-art"),
]
