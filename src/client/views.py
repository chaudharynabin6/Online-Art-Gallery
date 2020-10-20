from django.shortcuts import render, get_object_or_404, HttpResponse, redirect
from .models import client, artist
from .forms import client_update_form, artist_update_form
from artGallery.forms import art_add_or_update
from artGallery.models import art
# Create your views here.


def dashboard(request):
    user = request.user
    if(not(user.is_authenticated)):
        return render(request, "client/not-found.html", context={
            "error": "you must login as client or artist first"
        })
    else:
        current_client = client.objects.filter(user=request.user).first()
        if(current_client):
            if(current_client.mycart):
                arts = list(current_client.mycart.art_list.all())
            else:
                arts = []
            context = {
                "client": current_client,
                "arts":  arts
            }
            return render(request, "client/client-dashboard.html", context)
        else:
            current_artist = artist.objects.filter(user=request.user).first()
            context = {
                "artist": current_artist,
                "art_list": current_artist.art_list.all()
            }
            return render(request, "client/artist-dashboard.html", context)


def update_client_or_artist(request):

    if(not(request.user.is_authenticated)):
        return render(request, "client/not-found.html", context={
            "error": "you must login as client or artist first"
        })

    else:
        is_client_updated = False
        current_client = client.objects.filter(user=request.user).first()

        if(current_client):
            form = client_update_form(initial={
                "profile_photo": current_client.profile_photo,
                "first_name": current_client.first_name,
                "last_name": current_client.last_name,
                "bio": current_client.bio
            })
            if(request.method == "POST"):
                instace_client = get_object_or_404(client, user=request.user)
                form = client_update_form(
                    request.POST, request.FILES, instance=instace_client)
                if form.is_valid():
                    valid_client = form.save(commit=False)
                    valid_client.save()
                    is_client_updated = True
                    return redirect("client:dashboard")
                else:
                    return HttpResponse("client not updated")
            context = {
                "form": form,
                "client": current_client,
                "is_updated": is_client_updated,
            }

            return render(request, "client/update-client.html", context)

        else:
            is_artist_updated = False
            current_artist = artist.objects.filter(user=request.user).first()

            if(current_artist):
                form = artist_update_form(initial={
                    "profile_photo": current_artist.profile_photo,
                    "first_name": current_artist.first_name,
                    "last_name": current_artist.last_name,
                    "bio": current_artist.bio
                })
            if(request.method == "POST"):
                instace_artist = get_object_or_404(artist, user=request.user)
                form = artist_update_form(
                    request.POST, request.FILES, instance=instace_artist)
                if form.is_valid():
                    valid_artist = form.save(commit=False)
                    valid_artist.save()

                    print(form.cleaned_data)

                    is_artist_updated = True
                    return redirect("client:dashboard")
                else:
                    return HttpResponse("artist not updated")
            context = {
                "form": form,
                "artist": current_artist,
                "is_updated": is_artist_updated,
            }

            return render(request, "client/update-artist.html", context)


def add_art(request):
    current_artist = artist.objects.filter(user=request.user).first()
    if(current_artist):
        is_new_art_added = False
        form = art_add_or_update()
        if(request.method == "POST"):
            form = art_add_or_update(
                request.POST, request.FILES)
            if form.is_valid():
                new_art = form.save()
                current_artist.art_list.add(new_art)
                is_new_art_added = True
            else:
                print("invalid form")
        context = {
            "current_artist": current_artist,
            "form": form,
            "is_new_art_added": is_new_art_added,
        }
        return render(request, "client/add-art.html", context)
    else:
        context = {
            "error": "you must login as artist first"
        }
        return render(request, "client/not-found.html", context)
