# Generated by Django 4.2.1 on 2023-06-19 09:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('citys', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CityAreaModels',
            new_name='CityAreaModel',
        ),
        migrations.RenameModel(
            old_name='CityModels',
            new_name='CityModel',
        ),
    ]
