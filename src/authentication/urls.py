from django.urls import path, include
from .import views

app_name = "authentication"
urlpatterns = [
    # for signup
    path("signup", views.register, name="signup"),
    # for login feature
    path('', include("django.contrib.auth.urls")),
]
