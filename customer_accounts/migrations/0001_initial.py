# Generated by Django 3.2.20 on 2024-02-25 10:13

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="CustomerAccount",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "first_name",
                    models.CharField(
                        blank=True,
                        default="Information not provided",
                        max_length=30,
                    ),
                ),
                (
                    "last_name",
                    models.CharField(
                        blank=True,
                        default="Information not provided",
                        max_length=30,
                    ),
                ),
                (
                    "phone",
                    models.CharField(
                        blank=True,
                        max_length=30,
                        validators=[
                            django.core.validators.RegexValidator(
                                regex="^(((\\+44\\s?\\d{4}|\\(?0\\d{4}\\)?)\\s?\\d{3}\\s?\\d{3})|((\\+44\\s?\\d{3}|\\(?0\\d{3}\\)?)\\s?\\d{3}\\s?\\d{4})|((\\+44\\s?\\d{2}|\\(?0\\d{2}\\)?)\\s?\\d{4}\\s?\\d{4}))(\\s?\\#(\\d{4}|\\d{3}))?$"
                            )
                        ],
                    ),
                ),
                (
                    "address_line_1",
                    models.CharField(
                        default="Information not provided", max_length=60
                    ),
                ),
                (
                    "address_line_2",
                    models.CharField(
                        default="Information not provided", max_length=60
                    ),
                ),
                (
                    "city",
                    models.CharField(
                        default="Information not provided", max_length=60
                    ),
                ),
                (
                    "county",
                    models.CharField(
                        default="Information not provided", max_length=30
                    ),
                ),
                (
                    "post_code",
                    models.CharField(
                        default="Information not provided", max_length=30
                    ),
                ),
                ("birth_date", models.DateField(blank=True, null=True)),
                (
                    "gender",
                    models.CharField(
                        choices=[
                            ("M", "Male"),
                            ("F", "Female"),
                            ("O", "Other"),
                            ("N", "Prefer not to say"),
                        ],
                        default="N",
                        max_length=1,
                    ),
                ),
                (
                    "registration_date",
                    models.DateTimeField(default=django.utils.timezone.now),
                ),
                (
                    "memorable_name",
                    models.CharField(
                        default="Information not provided", max_length=60
                    ),
                ),
                ("memorable_date", models.DateField(blank=True, null=True)),
                (
                    "user",
                    models.OneToOneField(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
