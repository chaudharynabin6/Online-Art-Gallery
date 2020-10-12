from django.shortcuts import render, redirect
from .forms import RegisterForm
from client.models import client, artist
from django.contrib.auth.models import User
# Create your views here.


def register(request):
    '''
    the view function is called when user go the signup page

    since, signup is post request we first check 
    the request method is post to do sign up

    '''
    if request.method == "POST":  # if the request method is post then
        # converting the request.POST to form using RegisterForm class
        form = RegisterForm(request.POST)
        if form.is_valid():  # check is the form valid then

            # form is saved to the table specifed in RegisterForm Class
            user = form.save()
            if form.cleaned_data["client_or_artist"] == "True":
                client.objects.create(user=user)
            else:
                artist.objects.create(user=user)
            # finally reurning to /home url
            return redirect("/home")
    else:  # if the requset method is not post eg. get then
        # form is created
        form = RegisterForm()
    # finally redering the form in the signup page
    return render(request, "authentication/signup.html", {"form": form})
