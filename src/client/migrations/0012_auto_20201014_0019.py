# Generated by Django 3.0.5 on 2020-10-13 18:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0004_cart_art_list'),
        ('client', '0011_auto_20201013_2304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='mycart',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='cart.cart'),
        ),
    ]
