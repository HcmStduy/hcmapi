# Generated by Django 4.2.1 on 2023-06-18 06:52

from django.db import migrations, models
import user.models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_alter_appuser_img1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appuser',
            name='img1',
            field=models.ImageField(blank=True, null=True, upload_to=user.models.user_directory_path, verbose_name='头像'),
        ),
    ]
