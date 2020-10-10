from django.urls import path
from . import views
app_name = "artGallery"
urlpatterns = [
    path("", views.index, name="index")
]
