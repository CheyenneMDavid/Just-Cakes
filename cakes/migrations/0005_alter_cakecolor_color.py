# Generated by Django 3.2.20 on 2023-09-17 23:28

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("cakes", "0004_alter_individualcake_type"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cakecolor",
            name="color",
            field=models.CharField(max_length=50),
        ),
    ]
