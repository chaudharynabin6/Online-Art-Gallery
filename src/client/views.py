from django.shortcuts import render, get_object_or_404, HttpResponse
from .models import client, artist
from .forms import client_update_form, artist_update_form
# Create your views here.


def dashboard(request):
    user = request.user
    if(not(user.is_authenticated)):
        return render(request, "client/not-found.html")
    else:
        current_client = client.objects.filter(user=request.user).first()
        if(current_client.mycart):
            arts = list(current_client.mycart.art_list.all())
        else:
            arts = []
        if(current_client):
            context = {
                "client": current_client,
                "arts":  arts
            }
            return render(request, "client/client-dashboard.html", context)
        else:
            current_artist = artist.objects.filter(user=request.user)
            context = {
                "artist": current_artist.first()
            }
            return render(request, "client/artist-dashboard.html", context)


def update_client(request):

    if(not(request.user.is_authenticated)):
        return render(request, "client/not-found.html")

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
                    c = form.save(commit=False)
                    # c.user = request.user
                    c.save()
                    # client_instance = form.save(commit=False)
                    # client_instance.user = current_client.user
                    # client_instance.save(
                    #     update_fields=['profile_photo', 'bio', ])
                    print(form.cleaned_data)
                    # client.update()
                    # form.save()
                    # client.objects.filter(
                    #     user=request.user).(
                    #     first_name=data["first_name"],
                    #     last_name=data["last_name"],
                    #     profile_photo=data["profile_photo"],
                    #     bio=data["bio"])

                    is_client_updated = True
                else:
                    return HttpResponse("client not updated")
            context = {
                "form": form,
                "client": current_client,
                "is_updated": is_client_updated,
            }

            return render(request, "client/update-client.html", context)

        else:
            return render(request, "client/not-found.html")
