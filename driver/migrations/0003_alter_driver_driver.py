# Generated by Django 4.2.4 on 2023-08-13 12:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('driver', '0002_remove_driver_password_remove_driver_username_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driver',
            name='driver',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
