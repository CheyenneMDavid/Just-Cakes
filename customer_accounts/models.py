"""
Importing Regex to validate data.
Importing models in order to define the CustomerAccount model.
Importing get_user_model to interact with the default User model in Django.

Using text rather than default values, improving the UX, User not having to delete content in fields before filling their details in.
"""

from django.core.validators import RegexValidator
from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

# Importing and using "get_user_model" to allow flexibility and easier
# maintenance of the code in the future.
User = get_user_model()

# Credit for this regex pattern is StackOverflow at this page:
# https://stackoverflow.com/questions/25155970/
# validating-uk-phone-number-regex-c
phone_regex = RegexValidator(
    regex=r"^(((\+44\s?\d{4}|\(?0\d{4}\)?)\s?\d{3}\s?\d{3})|"
    r"((\+44\s?\d{3}|\(?0\d{3}\)?)\s?\d{3}\s?\d{4})|"
    r"((\+44\s?\d{2}|\(?0\d{2}\)?)\s?\d{4}\s?\d{4}))(\s?\#(\d{4}|\d{3}))?$",
)


class CustomerAccount(models.Model):
    """
    The CustomerAccount model is associated with the Django User model
    (from django-allauth) through a one-to-one relationship.
    This allows for the storage of extra user information without modifying
    the User model directly.
    """

    first_name = models.CharField(
        max_length=30, blank=True, help_text="Enter your first name"
    )
    last_name = models.CharField(
        max_length=30,
        blank=True,
        help_text="Enter your last name",
    )

    # Not using a default for the telephone field as it clashed with using
    # regex to validate entries, which included any meaningful default value
    # which suggested to the user that they enter the phone number.
    phone = models.CharField(
        max_length=30,
        validators=[phone_regex],
        blank=True,
    )

    # I've kept the character count pretty low because this only dealing
    # with UK addresses, so 60 is more than long enough.
    # The longest town in the uk is in wales and only has 58 letters.
    address_line_1 = models.CharField(
        max_length=60,
        blank=True,
        help_text="Please enter the first line of your address.",
    )
    address_line_2 = models.CharField(
        max_length=60,
        blank=True,
        help_text="Please enter the second line of your address",
    )
    city = models.CharField(
        max_length=60,
        blank=True,
        help_text="Please enter your city",
    )
    county = models.CharField(
        max_length=30, blank=True, help_text="Please enter your county"
    )
    post_code = models.CharField(
        max_length=30,
        blank=True,
        help_text="Please enter your postal code",
    )

    # Defines the accepted format of dates, when they are put in by the user.
    birth_date = models.DateField(
        null=True,
        blank=True,
        help_text="Please enter your D.O.B.",
    )

    # Gender selected by user.
    GENDER_CHOICES = [
        ("M", "Male"),
        ("F", "Female"),
        ("O", "Other"),
        ("N", "Prefer not to say"),
    ]
    gender = models.CharField(
        max_length=1,
        choices=GENDER_CHOICES,
        default="N",
    )

    registration_date = models.DateTimeField(default=timezone.now)

    # Both memorable name and memorable date can be used as security questions
    # if talking over the telephone.
    memorable_name = models.CharField(
        max_length=60,
        blank=True,
        help_text="Please enter a memorable name",
    )

    # Defines the accepted format of dates, when they are put in by the user.
    memorable_date = models.DateField(
        null=True,
        blank=True,
    )

    # Links the CustomerAccount model to the django-allauth.
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)

    # Returns the username.
    def __str__(self):
        return self.user.username
