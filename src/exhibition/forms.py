from django.forms import ModelForm
from django import forms
from django.forms.widgets import DateInput
from .models import exhibtion, art, auction


class add_update_art_form(ModelForm):

    class Meta:
        model = art
        fields = ["name", "photo", "video", "description", "minimum_price"]


class add_update_exhibition_form(ModelForm):

    class Meta:
        model = exhibtion
        fields = ["name", "exhibition_day", "exhibition_location"]
