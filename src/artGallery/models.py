from django.db import models
from utils.randomCode.getRandomCode import get_random_code
from django.template.defaultfilters import slugify
# Create your models here.


rating_choise = [(1, "1"), (2, "2"), (3, "3"), (4, "4"), (5, "5")]


class art(models.Model):
    art_name = models.CharField(max_length=200, blank=False)
    quality = models.IntegerField(choices=rating_choise, default=1)
    price = models.DecimalField(decimal_places=2, max_digits=20, blank=False)
    description = models.CharField(max_length=200, blank=False)
    art_slug = models.SlugField(
        unique=True, null=True, blank=True, editable=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    photo1 = models.ImageField(
        upload_to="photos/", blank=False)
    photo2 = models.ImageField(
        upload_to="photos/", blank=False)
    photo3 = models.ImageField(
        upload_to="photos/", blank=False)
    photo4 = models.ImageField(
        upload_to="photos/", blank=False)
    photo5 = models.ImageField(
        upload_to="photos/", blank=False)

    def __str__(self):
        return f"{self.art_slug}-{self.date_created.strftime('%d-%m-%y')}"

    def save(self, *args, **kwargs):
        slug = slugify(str(self.art_name))
        while(art.objects.filter(art_slug=slug).exists()):
            slug = slugify(str(self.art_name) + str(get_random_code()))

        self.art_slug = slug
        super().save(*args, **kwargs)
