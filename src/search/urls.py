from django.contrib.postgres import search
from django.urls import path
from .views import search_art
app_name = "search"
urlpatterns = [
    path("", search_art, name="search-art"),
]
