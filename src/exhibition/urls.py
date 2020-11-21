from django.urls import path
from .views import exhibition_hall
app_name = "exhibition"
urlpatterns = [
    path("", exhibition_hall, name="exhibition-hall")
    # path("add-to-cart", add_to_cart, name="add-to-cart")

]
