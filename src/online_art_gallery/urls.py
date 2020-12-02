"""online_art_gallery URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static
from .view import home_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", home_view, name="home"),
    # for signup and login feature
    path("authentication/", include("authentication.urls")),
    # for artGallery
    path("artgallery/", include("artGallery.urls")),
    path("dashboard/", include(("client.urls"))),
    path("exhibition/", include("exhibition.urls")),
    path("search/", include("search.urls"),),
    path("cart/", include("cart.urls")),

]

# this make the static file to load when were they are requested from url
urlpatterns += static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(
    settings.STATIC_URL, document_root=settings.STATIC_ROOT)
