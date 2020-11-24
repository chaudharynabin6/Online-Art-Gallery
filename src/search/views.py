from django.http.response import HttpResponse
from django.shortcuts import render
from django.contrib.postgres.search import TrigramSimilarity
from artGallery.models import art
from client.models import artist
# Create your views here.


def search_art(request):
    if(request.user.is_superuser):
        return render(request, "client/not-found.html", context={
            "error": "you must login as client or artist first"
        })
    current_artist = artist.objects.filter(user=request.user).first()
    if request.method == "GET" and current_artist and current_artist.art_list and request.GET.get("search_art"):
        search_art = request.GET.get("search_art")
        search_result_of_my_arts = current_artist.art_list.annotate(similarity=TrigramSimilarity(
            'art_name', search_art), ).filter(similarity__gt=0.3).order_by('-similarity')
        context = {
            "arts": search_result_of_my_arts
        }
        return render(request, "search/artist-art-search.html", context)

    elif request.method == "GET" and request.GET.get("search_art"):
        search_art = request.GET.get("search_art")
        search_result_arts = art.objects.annotate(
            similarity=TrigramSimilarity('art_name', search_art), ).filter(similarity__gt=0.3).order_by('-similarity')
        search_result_arts_with_artist = [(art, art.artist_set.all().first())
                                          for art in search_result_arts]
        context = {
            "arts": search_result_arts_with_artist
        }
        return render(request, "search\search.html", context)
    return render(request, "search\search.html")
