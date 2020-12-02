from django.http import request
from django.shortcuts import render
from client.models import client, artist
from django.db.models import Sum
# Create your views here.


def view_art_gallery_cart(request):
    user = request.user
    if(not(user.is_authenticated) or request.user.is_superuser):
        return render(request, "client/not-found.html", context={
            "error": "you must login as client or artist first"
        })
    else:
        current_client = client.objects.filter(user=request.user).first()
        if(current_client):
            if(current_client.mycart):
                # arts = list(current_client.mycart.art_list.all())
                total_price = current_client.mycart.art_list.all().aggregate(Sum('price'))[
                    'price__sum']
                arts = [(art, art.artist_set.all().first())
                        for art in current_client.mycart.art_list.all()]
                has_art = True

            else:
                arts = [],
                has_art = False
                total_price = 0
            context = {
                "client": current_client,
                "arts":  arts,
                "total_price": total_price,
                "has_art": has_art,
            }
            return render(request, "cart/cart.html", context)
        else:
            return render(request, "client/not-found.html", {
                "error": "you must be client"
            })
