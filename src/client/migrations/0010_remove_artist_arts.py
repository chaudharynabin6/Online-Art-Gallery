# Generated by Django 3.0.5 on 2020-10-13 15:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0009_auto_20201011_2209'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artist',
            name='arts',
        ),
    ]
