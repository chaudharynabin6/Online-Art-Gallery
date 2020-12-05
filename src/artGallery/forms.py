from django import forms
from .models import art


class art_add_or_update(forms.ModelForm):

    class Meta:
        model = art
        fields = ["art_name", "quality", "price", "description", "photo1",
                  "photo2", "photo3", "photo4", "photo5"]
