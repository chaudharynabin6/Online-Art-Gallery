from django.urls import path
from .views import dashboard, update_client_or_artist, add_art, client_profile, artist_profile, view_artist_profile
app_name = "client"
urlpatterns = [
    path("", dashboard, name="dashboard"),
    path("client-update", update_client_or_artist, name="client-update"),
    path("add-art", add_art, name="add-art"),
    path("client-profile", client_profile, name="client-profile"),
    path("artist-profile", artist_profile, name="artist-profile"),
    path("view-artist-profile/<str:artist_id>",
         view_artist_profile, name="view-artist-profile"),
]
