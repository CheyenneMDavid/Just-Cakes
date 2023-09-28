"""
Module Docstring:
I was continually receiving errors from pylint saying that the "imports"
should all have docstrings. I don't recall being taught to include them
for imports but am choosing to heed to warning from the linter and
including them.

This module contains forms related to the user operations such as signup.
It extends the default allauth forms to include extra fields.
"""
import re
from django import forms
from django.core.validators import RegexValidator
from allauth.account.forms import SignupForm


# In conjunction with the django documentation from here:
# https://django-allauth.readthedocs.io/en/latest/installation/quickstart.html
# I also gained help from following this YouTube
# tutorial: https://www.youtube.com/watch?v=dXZim_jgaiI&t=371s by Matt Freire
# on his Youtube channel here: https://www.youtube.com/@mattfreire

# The Regex pattern for this code is from the StackOverflow site, here:
# https://stackoverflow.com/questions/11518035/regular-expression-for-
# gb-based-and-only-numeric-phone-number.
pattern = re.compile(
    r"^(((\+44\s?\d{4}|\(?0\d{4}\)?)\s?\d{3}\s?\d{3})|"
    r"((\+44\s?\d{3}|\(?0\d{3}\)?)\s?\d{3}\s?\d{4})|"
    r"((\+44\s?\d{2}|\(?0\d{2}\)?)\s?\d{4}\s?\d{4}))(\s?\#(\d{4}|\d{3}))?$"
)


class CustomSignupForm(SignupForm):
    """
    This class represents a custom signup form which extends the default
    SignupForm provided by django-allauth. It includes additional fields
    to capture more information about the user during the signup process.
    """

    # Defining fields for the form, with their specification
    first_name = forms.CharField(max_length=50, label="First Name")
    last_name = forms.CharField(max_length=30, label="Last Name")
    username = forms.CharField(max_length=30, label="Username")
    birth_date = forms.DateField(label="Birthdate")

    # Choice field for gender with options.
    gender = forms.ChoiceField(
        choices=[
            ("M", "Male"),
            ("F", "Female"),
            ("O", "Other"),
            ("N", "Prefer not to say"),
        ],
        label="Gender",
    )

    # Phone Number field using regex to validator to ensure valid phone
    # number entry.
    phone_number = forms.CharField(
        validators=[
            RegexValidator(regex=pattern, message="Invalid Phone Number")
        ],
        max_length=15,
        label="Phone Number",
        required=False,
    )

    # All the address fields are optional. But as the application it further
    #  developed to incorporate actual ordering, these fields will be required.
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

    # Fields for preferred days of delivery.
    PREFERRED_DAYS_FOR_DELIVERY = [
        ("mon", "Monday"),
        ("tue", "Tuesday"),
        ("wed", "Wednesday"),
        ("thu", "Thursday"),
        ("fri", "Friday"),
    ]

    # Checking of the boxes for preferred days is optional. But as the
    # application it further developed to incorporate actual ordering, these
    # fields will be required.
    preferred_delivery_days = forms.MultipleChoiceField(
        choices=PREFERRED_DAYS_FOR_DELIVERY,
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )

    # Both the Interests field and also the Favorite Quotes fields are
    # optional. But as the application it further developed to incorporate
    # actual ordering, these fields will be required.
    interests = forms.CharField(
        max_length=255, label="Interests", required=False
    )
    favorite_quotes = forms.CharField(
        max_length=1000, label="Favorite Quotes", required=False
    )

    def save(self, request):
        """
        This saves the user object created by the form.
        """

        user = super().save(request)
        return user
