
from decimal import Context
from django.http.response import HttpResponse
from django.shortcuts import render
from client.models import client, artist
from django.db.models import Sum
from exhibition.models import exhibition, art as artClass, auction
from django.db.models import Max
from decimal import Decimal
# Create your views here.


def choose_cart(request):
    user = request.user
    if(not(user.is_authenticated) or request.user.is_superuser):
        return render(request, "client/not-found.html", context={
            "error": "you must login as client or artist first"
        })
    else:
        current_client = client.objects.filter(user=request.user).first()
        if(current_client):
            return render(request, "cart/cart.html")
        else:
            return render(request, "client/not-found.html", {
                "error": "you must be client"
            })


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
            return render(request, "cart/cart-art-gallery.html", context)
        else:
            return render(request, "client/not-found.html", {
                "error": "you must be client"
            })


def create_cart_from_exhibition():
    """
    get the client,art,auction,
    """
    max_auction_list = []
    ex = exhibition.objects.filter(is_active=True).first()
    if(ex):
        approved_arts = artClass.objects.filter(
            exhibition=ex, is_approved=True)
        if(approved_arts):
            for art in approved_arts.iterator():
                auctions = auction.objects.filter(art=art)
                if(auctions):
                    max_auction = auctions.order_by('-bid_amount')[0]
                    max_auction_list.append(max_auction)

            return max_auction_list


def exhibition_cart(request):
    if not request.user.is_authenticated or request.user.is_superuser:
        return render(request, "exhibition/not-found.html", {
            "error": "you must login as client"
        })
    current_client = client.objects.filter(user=request.user).first()
    if(current_client):
        my_auctions = []
        total_amount = Decimal(0)
        max_auction_list = create_cart_from_exhibition()
        if(max_auction_list):
            for item in max_auction_list:
                my_auc = item.client == current_client
                if(my_auc):
                    my_auctions.append(item)
                    total_amount += item.bid_amount

        context = {
            "my_auctions": my_auctions,
            "total_amount": total_amount,
            "has_art": bool(my_auctions),
        }
        print(context)
        return render(request, "cart/exhibition-cart.html", context)
    else:
        return render(request, "client/not-found.html", {
            "error": "you must be client"
        })
