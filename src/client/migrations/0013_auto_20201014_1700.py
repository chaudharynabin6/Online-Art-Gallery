# Generated by Django 3.0.5 on 2020-10-14 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0012_auto_20201014_0019'),
    ]

    operations = [
        migrations.AddField(
            model_name='artist',
            name='first_name',
            field=models.CharField(blank=True, max_length=32),
        ),
        migrations.AddField(
            model_name='artist',
            name='last_name',
            field=models.CharField(blank=True, max_length=32),
        ),
        migrations.AddField(
            model_name='client',
            name='first_name',
            field=models.CharField(blank=True, max_length=32),
        ),
        migrations.AddField(
            model_name='client',
            name='last_name',
            field=models.CharField(blank=True, max_length=32),
        ),
    ]