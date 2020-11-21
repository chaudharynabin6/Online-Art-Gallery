from django.urls import path
from .views import exhibition_hall, add_art
app_name = "exhibition"
urlpatterns = [
    path("", exhibition_hall, name="exhibition-hall"),
    path("add-art", add_art, name="add-art")

]
