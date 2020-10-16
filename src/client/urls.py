from django.urls import path
from .views import dashboard, update_client
app_name = "client"
urlpatterns = [
    path("", dashboard, name="dashboard"),
    path("client-update", update_client, name="client-update")
]
