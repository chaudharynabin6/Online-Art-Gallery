from django.shortcuts import render

# Create your views here.


def exhibition_hall(request):
    """
    This function is home for the exhibition hall
    """
    return render(request, "exhibition/exhibition-hall.html")
