# Generated by Django 3.2.20 on 2023-09-17 18:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("cakes", "0003_auto_20230908_0424"),
    ]

    operations = [
        migrations.AlterField(
            model_name="individualcake",
            name="type",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT, to="cakes.caketype"
            ),
        ),
    ]
