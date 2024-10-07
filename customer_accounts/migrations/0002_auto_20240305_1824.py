# Generated by Django 3.2.20 on 2024-03-05 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("customer_accounts", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customeraccount",
            name="address_line_1",
            field=models.CharField(
                blank=True,
                help_text="Please enter the first line of your address.",
                max_length=60,
            ),
        ),
        migrations.AlterField(
            model_name="customeraccount",
            name="address_line_2",
            field=models.CharField(
                blank=True,
                help_text="Please enter the second line of your address",
                max_length=60,
            ),
        ),
        migrations.AlterField(
            model_name="customeraccount",
            name="birth_date",
            field=models.DateField(
                blank=True, help_text="Please enter your D.O.B.", null=True
            ),
        ),
        migrations.AlterField(
            model_name="customeraccount",
            name="city",
            field=models.CharField(
                blank=True, help_text="Please enter your city", max_length=60
            ),
        ),
        migrations.AlterField(
            model_name="customeraccount",
            name="county",
            field=models.CharField(
                blank=True,
                help_text="Please enter your county",
                max_length=30,
            ),
        ),
        migrations.AlterField(
            model_name="customeraccount",
            name="first_name",
            field=models.CharField(
                blank=True, help_text="Enter your first name", max_length=30
            ),
        ),
        migrations.AlterField(
            model_name="customeraccount",
            name="last_name",
            field=models.CharField(
                blank=True, help_text="Enter your last name", max_length=30
            ),
        ),
        migrations.AlterField(
            model_name="customeraccount",
            name="memorable_name",
            field=models.CharField(
                blank=True,
                help_text="Please enter a memorable name",
                max_length=60,
            ),
        ),
        migrations.AlterField(
            model_name="customeraccount",
            name="post_code",
            field=models.CharField(
                blank=True,
                help_text="Please enter your postal code",
                max_length=30,
            ),
        ),
    ]
