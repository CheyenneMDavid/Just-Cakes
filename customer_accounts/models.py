"""
Importing Regex to validate data.
Importing models in order to define the CustomerAccount model.
Importing get_user_model to interact with the default User model in Django.

"""

from django.core.validators import RegexValidator
from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

# Importing and using "get_user_model" to allow flexibility and easier
# maintenance of the code in the future.
User = get_user_model()


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
        max_length=30,
        blank=True,
        default="Information not provided",
    )
    last_name = models.CharField(
        max_length=30,
        blank=True,
        default="Information not provided",
    )

    phone = models.CharField(
        max_length=15,
        validators=[phone_regex],
        blank=True,
    )

    # I've kept the character count pretty low because this only dealing
    # with UK addresses, so 60 is more than long enough.
    # The longest town in the uk is in wales and only has 58 letters.
    address_line_1 = models.CharField(
        max_length=60,
        default="Information not provided",
    )
    address_line_2 = models.CharField(
        max_length=60,
        default="Information not provided",
    )
    city = models.CharField(
        max_length=60,
        default="Information not provided",
    )
    county = models.CharField(
        max_length=20,
        default="Information not provided",
    )
    post_code = models.CharField(
        max_length=15,
        default="Information not provided",
    )

    # Defines the accepted format of dates, when they are put in by the user.
    birth_date = models.DateField(null=True, blank=True)

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
        default="Information not provided",
    )

    # Defines the accepted format of dates, when they are put in by the user.
    memorable_date = models.DateField(blank=True, null=True)

    # Links the CustomerAccount model to the django-allauth.
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)

    # Returns the username.
    def __str__(self):
        return self.user.username
