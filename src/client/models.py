from django.db import models
from django.contrib.auth.models import User
from cart.models import cart
from artGallery.models import art
from django.template.defaultfilters import slugify

# Create your models here.


class client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=False)
    first_name = models.CharField(max_length=32, blank=True)
    last_name = models.CharField(max_length=32, blank=True)
    profile_photo = models.ImageField(
        default="profile.png", upload_to='profile/')
    bio = models.CharField(max_length=200, default="no bio...")
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True, blank=True, null=True, editable=False)
    is_client = models.BooleanField(choices=[(True, "yes"), ], default=True)
    mycart = models.OneToOneField(
        cart, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return f"{self.user.username}-{self.date_created.strftime('%d-%m-%Y')}"

    def save(self, *args, **kargs):
        self.slug = slugify(str(self.user.username))
        super().save(*args, **kargs)

    def get_user_email(self):
        return self.user.email


class artist(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=False)
    art_list = models.ManyToManyField(
        art, blank=True, null=True)
    first_name = models.CharField(max_length=32, blank=True)
    last_name = models.CharField(max_length=32, blank=True)
    profile_photo = models.ImageField(
        default="profile.png", upload_to='profile/')
    bio = models.CharField(max_length=200, default="no bio...")
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True, blank=True, null=True)
    is_artist = models.BooleanField(choices=[(True, "Yes"), ], default=True)

    def __str__(self):
        return f"{self.user.username}-{self.date_created.strftime('%d-%m-%Y')}"

    def save(self, *args, **kargs):
        self.slug = slugify(str(self.user.username))
        super().save(*args, **kargs)

    def get_user_email(self):
        return f"{self.user.email}"
