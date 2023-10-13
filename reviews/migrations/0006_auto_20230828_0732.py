# Generated by Django 3.2.20 on 2023-08-28 07:32

import cloudinary.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("reviews", "0005_alter_reviews_featured_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="reviews",
            name="excerpt",
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name="reviews",
            name="updated_on",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name="reviews",
            name="featured_image",
            field=cloudinary.models.CloudinaryField(
                default="placeholder", max_length=255, verbose_name="image"
            ),
        ),
        migrations.AlterField(
            model_name="reviews",
            name="likes",
            field=models.ManyToManyField(
                blank=True, related_name="reviewspost_like", to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
