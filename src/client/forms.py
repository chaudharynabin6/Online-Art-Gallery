from django.forms import ModelForm
from django import forms
from .models import client, artist


class client_update_form(ModelForm):

    bio = forms.CharField(widget=forms.Textarea(attrs={"rows": "2"}))

    class Meta:
        model = client
        fields = ["profile_photo", "bio", "first_name", "last_name"]

    # def save(self, commit=False):
    #     user = self.instance
    #     user.bio = self.cleaned_data["bio"]
    #     user.profile_photo = self.cleaned_data["profile_photo"]
    #     user.first_name = self.cleaned_data["first_name"]
    #     user.last_name = self.cleaned_data["last_name"]
    #     user.save()
    #     return user


class artist_update_form(ModelForm):

    class Meta:
        model = artist
        fields = ["profile_photo", "bio", "first_name", "last_name"]
