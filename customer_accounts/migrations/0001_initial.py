# Generated by Django 3.2.20 on 2023-09-08 04:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=12)),
                ('address_line_1', models.CharField(max_length=50)),
                ('address_line_2', models.CharField(max_length=60)),
                ('city', models.CharField(max_length=60)),
                ('county', models.CharField(max_length=20)),
                ('post_code', models.CharField(max_length=15)),
                ('account_number', models.CharField(max_length=20, unique=True)),
                ('registration_date', models.DateTimeField(auto_now_add=True)),
                ('payment_method', models.CharField(max_length=50)),
                ('basket_item_count', models.IntegerField(default=0)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
