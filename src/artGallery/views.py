from django.shortcuts import render

# Create your views here.
from .models import art


def index(request):
    return render(request, "artgallery/index.html", {
        "arts": art.objects.all()
    })
