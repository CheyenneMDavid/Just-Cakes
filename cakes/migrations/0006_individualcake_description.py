# Generated by Django 3.2.20 on 2023-09-19 01:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cakes', '0005_alter_cakecolor_color'),
    ]

    operations = [
        migrations.AddField(
            model_name='individualcake',
            name='description',
            field=models.TextField(default=''),
        ),
    ]
