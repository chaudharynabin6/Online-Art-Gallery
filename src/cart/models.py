from django.db import models
from artGallery.models import art
from utils.randomCode.getRandomCode import get_random_code
from django.template.defaultfilters import slugify
# Create your models here.


class cart(models.Model):
    arts = models.ManyToManyField(art, related_name="cart_art")
    cart_slug = models.SlugField(
        unique=True, null=True, blank=True, editable=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.cart_slug}--{self.date_created.strftime('%d-%m-%y')}"

    def save(self, *args, **kwargs):
        slug = slugify(str(get_random_code()))
        while(cart.objects.filter(cart_slug=slug).exists()):
            slug = slugify(str(get_random_code()))

        self.cart_slug = slug
        super().save(*args, **kwargs)
