from django.urls import path
from .views import dashboard, update_client_or_artist
app_name = "client"
urlpatterns = [
    path("", dashboard, name="dashboard"),
    path("client-update", update_client_or_artist, name="client-update")
]
