# Generated by Django 5.0.1 on 2024-01-10 06:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='WeatherCache',
            new_name='Weather',
        ),
    ]
