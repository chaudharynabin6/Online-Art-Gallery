from django.db import models

# Create your models here.


rating_choise = [(1, "1"), (2, "2"), (3, "3"), (4, "4"), (5, "5")]


class art(models.Model):
    art_name = models.CharField(max_length=200, blank=False)
    rating = models.IntegerField(choices=rating_choise, default=1)
    price = models.DecimalField(decimal_places=2, max_digits=20, blank=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    photo1 = models.ImageField(
        upload_to="photos/", blank=False, default="profile.png")
    photo2 = models.ImageField(
        upload_to="photos/", blank=False, default="profile.png")
    photo3 = models.ImageField(
        upload_to="photos/", blank=False, default="profile.png")
    photo4 = models.ImageField(
        upload_to="photos/", blank=False, default="profile.png")
    photo5 = models.ImageField(
        upload_to="photos/", blank=False, default="profile.png")

    def __str__(self):
        return f"{self.art_name}-{self.date_created.strftime('%d-%m-%y')}"
