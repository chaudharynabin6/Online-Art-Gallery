# Generated by Django 3.0.5 on 2020-10-13 17:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0004_cart_art_list'),
        ('artGallery', '0004_auto_20201013_2304'),
        ('client', '0010_remove_artist_arts'),
    ]

    operations = [
        migrations.AddField(
            model_name='artist',
            name='art_list',
            field=models.ManyToManyField(blank=True, null=True, to='artGallery.art'),
        ),
        migrations.RemoveField(
            model_name='client',
            name='mycart',
        ),
        migrations.AddField(
            model_name='client',
            name='mycart',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cart.cart'),
        ),
    ]
