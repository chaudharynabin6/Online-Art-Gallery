from django.shortcuts import render, redirect
from .forms import RegisterForm

# Create your views here.


def register(response):
    '''
    the view function is called when user go the signup page

    since, signup is post request we first check 
    the response method is post to do sign up

    '''
    if response.method == "POST":  # if the request method is post then
        # converting the response.POST to form using RegisterForm class
        form = RegisterForm(response.POST)
        if form.is_valid():  # check is the form valid then
            # form is saved to the table specifed in RegisterForm Class
            form.save()
            # finally reurning to /home url
            return redirect("/home")
    else:  # if the requset method is not post eg. get then
        # form is created
        form = RegisterForm()
    # finally redering the form in the signup page
    return render(response, "signup.html", {"form": form})
