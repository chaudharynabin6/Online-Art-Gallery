from django.forms import ModelForm
from django import forms
from .models import exhibtion, art, auction


class add_update_art_form(ModelForm):

    class Meta:
        model = art
        fields = ["name", "photo", "video", "description", "minimum_price"]
