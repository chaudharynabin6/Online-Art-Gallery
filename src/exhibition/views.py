from django.http import request
from django.shortcuts import redirect, render
from .forms import add_update_art_form
from client.models import client, artist
from .models import exhibtion, art, auction
from django.contrib.auth.models import User
# Create your views here.


def exhibition_hall(request):
    """
    This function is home for the exhibition hall
    """
    if(artist.objects.filter(user=request.user).first()):
        is_artist = True
    else:
        is_artist = False

    if(request.user.is_superuser):
        arts = art.objects.filter(is_approved=False).order_by('date_created')
    elif artist.objects.filter(user=request.user).first():
        arts = art.objects.filter(
            artist=artist.objects.filter(user=request.user).first())

    else:
        arts = art.objects.filter(is_approved=True)
    context = {
        "arts": arts,
        "is_artist": is_artist
    }
    return render(request, "exhibition/exhibition-hall.html", context)


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
            return redirect("exhibition:exhibition-hall")
        context = {
            "form": form
        }
        return render(request, "exhibition/add-update-art.html", context)

    else:
        return render(request, "exhibition/not-found.html", {"error": "this feature is only available to artist"})


def art_showcase(request, art_id):

    current_art = art.objects.filter(id=art_id).first()
    print(current_art)
    context = {
        "art": current_art
    }
    return render(request, "exhibition/art-showcase.html", context)


def approve_art(request):
    if(request.user.is_superuser and request.method == "POST"):
        art_id = request.POST.get('art_id')
        art_obj = art.objects.get(id=art_id)
        art_obj.is_approved = True
        art_obj.save()
        return redirect("exhibition:exhibition-hall")
