# Generated by Django 3.2.20 on 2024-03-26 01:56

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("customer_accounts", "0003_alter_customeraccount_gender"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customeraccount",
            name="address_line_1",
            field=models.CharField(
                blank=True,
                help_text="Please enter the first line of your address.",
                max_length=60,
                validators=[
                    django.core.validators.RegexValidator(
                        regex="^[a-zA-Z0-9\\s-]*$"
                    )
                ],
            ),
        ),
        migrations.AlterField(
            model_name="customeraccount",
            name="address_line_2",
            field=models.CharField(
                blank=True,
                help_text="Please enter the second line of your address",
                max_length=60,
                validators=[
                    django.core.validators.RegexValidator(
                        regex="^[a-zA-Z0-9\\s-]*$"
                    )
                ],
            ),
        ),
        migrations.AlterField(
            model_name="customeraccount",
            name="post_code",
            field=models.CharField(
                blank=True,
                help_text="Please enter your postal code",
                max_length=30,
                validators=[
                    django.core.validators.RegexValidator(
                        regex="^([Gg][Ii][Rr] 0[Aa]{2})|((([A-Za-z][0-9]{1,2})|(([A-Za-z][A-Ha-hJ-Yj-y][0-9]{1,2})|(([A-Za-z][0-9][A-Za-z])|([A-Za-z][A-Ha-hJ-Yj-y][0-9][A-Za-z]?))))\\s?[0-9][A-Za-z]{2})"
                    )
                ],
            ),
        ),
    ]
