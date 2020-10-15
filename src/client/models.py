from django.db import models
from django.contrib.auth.models import User
from artGallery.models import art
from cart.models import cart
from django.template.defaultfilters import slugify

# Create your models here.


class client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=False)
    profile_photo = models.ImageField(
        default="profile.png", upload_to='profile/')
    bio = models.CharField(max_length=200, default="no bio...")
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True, blank=True, null=True, editable=False)
    is_client = models.BooleanField(choices=[(True, "yes"), ], default=True)
    mycart = models.ManyToManyField(
        cart, blank=True)

    def __str__(self):
        return f"{self.user.username}-{self.date_created.strftime('%d-%m-%Y')}"

    def save(self, *args, **kargs):
        self.slug = slugify(str(self.user.username))
        super().save(*args, **kargs)

    def get_user_email(self):
        return self.user.email


class artist(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=False)
    profile_photo = models.ImageField(
        default="profile.png", upload_to='profile/')
    bio = models.CharField(max_length=200, default="no bio...")
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True, blank=True, null=True)
    is_artist = models.BooleanField(choices=[(True, "Yes"), ], default=True)
    arts = models.ForeignKey(
        art, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.user.username}-{self.date_created.strftime('%d-%m-%Y')}"

    def save(self, *args, **kargs):
        self.slug = slugify(str(self.user.username))
        super().save(*args, **kargs)

    def get_user_email(self):
        return f"{self.user.email}"
