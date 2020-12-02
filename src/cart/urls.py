from django.urls import path
from .views import view_art_gallery_cart
app_name = "cart"
urlpatterns = [
    path("", view_art_gallery_cart, name="cart"),
]
