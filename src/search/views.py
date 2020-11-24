from django.http.response import HttpResponse
from django.shortcuts import render
from django.contrib.postgres.search import TrigramSimilarity
from artGallery.models import art
# Create your views here.


def search_art(request):
    if request.method == "GET" and request.GET.get("search_art"):
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
