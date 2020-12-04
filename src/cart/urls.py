from django.urls import path
from .views import view_art_gallery_cart, exhibition_cart, choose_cart
app_name = "cart"
urlpatterns = [
    path("", choose_cart, name="cart"),
    path("exhibition-cart", exhibition_cart, name="exhibition-cart"),
    path("art-gallery-cart", view_art_gallery_cart, name="art-gallery-cart")
]
