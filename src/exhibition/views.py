from django.http import request
from django.shortcuts import render
from .forms import add_update_art_form
from client.models import client, artist
from .models import exhibtion
# Create your views here.


def exhibition_hall(request):
    """
    This function is home for the exhibition hall
    """
    return render(request, "exhibition/exhibition-hall.html")


def add_art(request):
    current_artist = artist.objects.filter(user=request.user).first()
    if(current_artist):
        form = add_update_art_form()
        if request.method == "POST":
            form = add_update_art_form(request.POST, request.FILES)
            current_art = form.save(commit=False)
            current_art.exhibtion = exhibtion.objects.first()
            current_art.artist = current_artist
            current_art.save()
            return render(request, "exhibition/exhibition-hall.html")
        context = {
            "form": form
        }
        return render(request, "exhibition/add-update-art.html", context)

    else:
        return render(request, "exhibition/not-found.html", {"error": "this feature is only available to artist"})
