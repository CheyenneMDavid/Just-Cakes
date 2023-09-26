"""
Module Docstring:
This module contains forms related to the user operations such as signup.
It extends the default allauth forms to include extra fields.
"""
from django import forms
from django.core.validators import RegexValidator
from allauth.account.forms import SignupForm


# In conjunction with the django documentation from here:
# https://django-allauth.readthedocs.io/en/latest/installation/quickstart.html
# I also gained help from following this YouTube
# tutorial: https://www.youtube.com/watch?v=dXZim_jgaiI&t=371s by Matt Freire
# on his Youtube channel here: https://www.youtube.com/@mattfreire


class CustomSignupForm(SignupForm):
    """
    This class represents a custom signup form which extends the default
    SignupForm provided by django-allauth. It includes additional fields
    to capture more information about the user during the signup process.
    """

    first_name = forms.CharField(max_length=50, label="First Name")
    last_name = forms.CharField(max_length=30, label="Last Name")
    username = forms.CharField(max_length=30, label="Username")
    birth_date = forms.DateField(label="Birthdate")
    gender = forms.ChoiceField(
        choices=[
            ("M", "Male"),
            ("F", "Female"),
            ("O", "Other"),
            ("N", "Prefer not to say"),
        ],
        label="Gender",
    )
    phone_number = forms.CharField(
        validators=[
            RegexValidator(regex=r"^[\d]+$", message="Invalid Phone Number")
        ],
        max_length=15,
        label="Phone Number",
        required=False,
    )
    address_line1 = forms.CharField(
        max_length=50, label="Address Line 1", required=False
    )
    address_line2 = forms.CharField(
        max_length=50, label="Address Line 2", required=False
    )
    city = forms.CharField(max_length=30, label="City", required=False)
    county = forms.CharField(
        max_length=20, label="State/Province", required=False
    )
    post_code = forms.CharField(
        max_length=12, label="Postal Code", required=False
    )

    PREFERRED_DAYS_FOR_DELIVERY = [
        ("mon", "Monday"),
        ("tue", "Tuesday"),
        ("wed", "Wednesday"),
        ("thu", "Thursday"),
        ("fri", "Friday"),
    ]

    preferred_delivery_days = forms.MultipleChoiceField(
        choices=PREFERRED_DAYS_FOR_DELIVERY,
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )

    interests = forms.CharField(
        max_length=255, label="Interests", required=False
    )

    favorite_quotes = forms.CharField(max_length=1000, label="Favorite Quotes")

    def save(self, request):
        user = super().save(request)

        return user
