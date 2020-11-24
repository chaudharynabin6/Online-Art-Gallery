from django.http import request
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from .forms import add_update_art_form, add_update_exhibition_form
from client.models import client, artist
from .models import exhibition, art, auction as auc
from django.contrib.auth.models import User
from django.db.models import Max
from decimal import Context, Decimal
# Create your views here.


def exhibition_hall(request):
    """
    This function is home for the exhibition hall
    """
    ex = exhibition.objects.filter(is_active=True).first()

    if(ex):
        is_exhibition = True
    else:
        is_exhibition = False
    if not request.user.is_authenticated:
        return render(request, "exhibition/not-found.html", {
            "error": "you must login first"
        })
    # is artist or not
    if(artist.objects.filter(user=request.user).first()):
        is_artist = True
    else:
        is_artist = False
    # if admin login
    if(request.user.is_superuser):
        arts = art.objects.filter(exhibition=ex,
                                  is_approved=False).order_by('date_created')
    # if artist login
    elif artist.objects.filter(user=request.user).first():
        arts = art.objects.filter(exhibition=ex,
                                  artist=artist.objects.filter(user=request.user).first())

    else:
        #  if client logined
        arts = art.objects.filter(exhibition=ex, is_approved=True)
    context = {
        "arts": arts,
        "is_artist": is_artist,
        "is_exhibition": is_exhibition
    }
    return render(request, "exhibition/exhibition-hall.html", context)


def add_art(request):
    ex = exhibition.objects.filter(is_active=True).first()
    current_artist = artist.objects.filter(user=request.user).first()
    if(current_artist):
        form = add_update_art_form()
        if request.method == "POST":
            form = add_update_art_form(request.POST, request.FILES)
            current_art = form.save(commit=False)
            current_art.exhibition = ex
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
    ex = exhibition.objects.filter(is_active=True).first()
    if not request.user.is_authenticated:
        return render(request, "exhibition/not-found.html", {
            "error": "you must login first"
        })
    current_art = art.objects.filter(exhibition=ex, id=art_id).first()
    top_5_auctions = auc.objects.filter(
        art=current_art).order_by("-bid_amount")[:5]
    if(client.objects.filter(user=request.user)):
        is_client = True
    else:
        is_client = False
    context = {
        "art": current_art,
        "is_client": is_client,
        "top_5_auctions": top_5_auctions
    }
    return render(request, "exhibition/art-showcase.html", context)


def approve_art(request):
    ex = exhibition.objects.filter(is_active=True).first()
    if(request.user.is_superuser and request.method == "POST"):
        art_id = request.POST.get('art_id')
        art_obj = art.objects.filter(exhibition=ex, id=art_id).first()
        art_obj.is_approved = True
        art_obj.save()
        return redirect("exhibition:exhibition-hall")
    else:
        return render(request, "exhibition/not-found.html", {
            "error": "you are not the adminstrator user"
        })


def auction(request):
    if not request.user.is_authenticated:
        return render(request, "exhibition/not-found.html", {
            "error": "you must login first"
        })
    current_client = client.objects.filter(user=request.user).first()
    if(current_client and request.method == "POST"):
        bid_amount = request.POST.get('bid_amount')
        art_id = request.POST.get('art_id')
        current_art = art.objects.filter(id=art_id).first()
        max_bid = auc.objects.filter(
            art=current_art).aggregate(Max('bid_amount'))["bid_amount__max"]
        if(max_bid):
            if (Decimal(bid_amount) > Decimal(current_art.minimum_price)):
                auc.objects.create(
                    art=current_art, client=current_client, bid_amount=Decimal(bid_amount))
                current_art.minimum_price = Decimal(bid_amount)
                current_art.save()
            else:
                return render(request, "exhibition/not-found.html", {
                    "error": "you must increase bid than current bid"
                })

        elif Decimal(bid_amount) > current_art.minimum_price:
            auc.objects.create(
                art=current_art, client=current_client, bid_amount=Decimal(bid_amount))
            current_art.minimum_price = Decimal(bid_amount)
            current_art.save()

        else:
            return render(request, "exhibition/not-found.html", {
                "error": "you must increase bid than current bid"
            })

    return redirect("exhibition:art-showcase", art_id)


def add_exhibition(request):
    if(request.user.is_superuser):
        form = add_update_exhibition_form()
        if(request.method == "POST"):
            form = add_update_exhibition_form(request.POST)
            form.save()
            return redirect("exhibition:manage-exhibition")
        context = {
            "form": form
        }
        return render(request, "exhibition/add-update-exhibition.html", context)
    else:
        return render(request, "exhibition/not-found.html", {
            "error": "you must be administrator for adding exhibition"
        })


def manage_exhibition(request):
    if(request.user.is_superuser):
        exhibitions = exhibition.objects.all()
        context = {
            "exhibitions": exhibitions,
        }
        return render(request, "exhibition/manage-exhibition.html", context)
    else:
        return render(request, "exhibition/not-found", {
            "error": "you must be super user to manage the exhibition"
        })


def activate_exhibition(request):
    if(request.user.is_superuser and request.method == "POST"):
        exhibition_id = request.POST.get("exhibition_id")
        current_exhibition = exhibition.objects.filter(
            id=exhibition_id).first()
        if(current_exhibition):
            current_exhibition.is_active = True
            current_exhibition.save()
            exhibition.objects.exclude(
                id=exhibition_id).update(is_active=False)
            return redirect("exhibition:manage-exhibition")
    else:
        return render(request, "exhibition/not-found.html", {
            "error": "you must be administrator for adding exhibition"
        })


def deactivate_exhibition(request):
    if(request.user.is_superuser and request.method == "POST"):
        exhibition_id = request.POST.get("exhibition_id")
        current_exhibition = exhibition.objects.filter(
            id=exhibition_id).first()
        if(current_exhibition):
            current_exhibition.is_active = False
            current_exhibition.save()
        return redirect("exhibition:manage-exhibition")
    else:
        return render(request, "exhibition/not-found.html", {
            "error": "you must be administrator for adding exhibition"
        })
