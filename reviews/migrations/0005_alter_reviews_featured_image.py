# Generated by Django 3.2.20 on 2023-08-28 07:07

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("reviews", "0004_reviews_featured_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="reviews",
            name="featured_image",
            field=models.ImageField(default="default_image.jpg", upload_to="images/"),
        ),
    ]
