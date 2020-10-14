from django.urls import path
from .views import home, add_to_cart
app_name = "artGallery"
urlpatterns = [
    path("", home, name="home"),
    path("add-to-cart", add_to_cart, name="add-to-cart")

]
