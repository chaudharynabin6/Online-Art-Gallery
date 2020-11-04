from django.shortcuts import redirect, render
from .models import art
from client.models import client, artist
from cart.models import cart
from django.http import HttpResponse

# Create your views here.


def home(request):
    if(not(request.user.is_authenticated)):
        arts = [(art, art.artist_set.all().first())
                for art in art.objects.all()]
        print(arts)
        return render(request, "artgallery/index.html", {
            "arts": arts,
        })
    else:
        client_user = client.objects.filter(user=request.user)
        arts = [(art, art.artist_set.all().first())
                for art in art.objects.all()]
        if(client_user):
            # for client user
            return render(request, "artgallery/index.html", {

                "arts": arts,
            })
        else:
            return HttpResponse("you must login as client first or logout first")


def add_to_cart(request):
    user = request.user
    if request.method == 'POST':
        art_id = request.POST.get('art_id')
        art_obj = art.objects.get(id=art_id)
        current_client = client.objects.get(user=user)
        client_cart = current_client.mycart
        print(client_cart)
        print(current_client)

        if(client_cart):
            if art_obj not in current_client.mycart.art_list.all():
                current_client.mycart.art_list.add(art_obj)

        else:
            current_user_cart = cart()
            current_user_cart.save()
            current_user_cart.art_list.add(art_obj)
            current_client.mycart = current_user_cart
            current_client.save()

        return redirect("artGallery:home")

        # if profile in post_obj.liked.all():
        #     post_obj.liked.remove(profile)
        # else:
        #     post_obj.liked.add(profile)

        # cart, created = cart.objects.get_or_create(art_list=art_id)

        # if not created:
        #     if like.value == 'Like':
        #         like.value = 'Unlike'
        #     else:
        #         like.value = 'Like'
        # else:
        #     like.value = 'Like'

        #     post_obj.save()
        #     like.save()
