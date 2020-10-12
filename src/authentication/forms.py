from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    '''
    inherits the UserCreationForm

    this class is used for extending the UserCreationForm
    helps to specify which field i like when we render form
    '''
    email = forms.EmailField()
    client_or_artist = forms.ChoiceField(
        choices=[(True, "client"), (False, "artist")],
        required=True
    )

    # meta class is used to descrive the extra information about class
    class Meta:
        # uses User Class as model
        model = User
        # and this fields is used to specify which input fields going to
        # render in signup page
        fields = ["username", "email",
                  "client_or_artist", "password1", "password2"]
