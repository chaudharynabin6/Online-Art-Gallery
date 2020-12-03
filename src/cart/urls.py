from django.urls import path
from .views import view_art_gallery_cart, exhibition_cart
app_name = "cart"
urlpatterns = [
    path("", view_art_gallery_cart, name="cart"),
    path("exhibition-cart", exhibition_cart, name="exhibition-cart")
]
