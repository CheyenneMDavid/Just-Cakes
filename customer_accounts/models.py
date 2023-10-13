"""
Importing Regex to validate data.
Importing models in order to define the CustomerAccount model.
Importing get_user_model to interact with the default User model in Django.

"""
from django.core.validators import RegexValidator
from django.db import models
from django.contrib.auth import get_user_model

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

    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)

    phone = models.CharField(max_length=15, validators=[phone_regex])

    # I've kept the character count pretty low because this only dealing
    # with UK addresses, so 60 is more than long enough.
    # The longest town in the uk is in wales and only has 58 letters.
    address_line_1 = models.CharField(max_length=60)
    address_line_2 = models.CharField(max_length=60)
    city = models.CharField(max_length=60)
    county = models.CharField(max_length=20)
    post_code = models.CharField(max_length=15)

    # Defines the accepted format of dates, when they are put in by the user.
    birth_date = models.DateField(null=True, blank=True)

    # Gender selected by user.
    GENDER_CHOICES = [
        ("M", "Male"),
        ("F", "Female"),
        ("O", "Other"),
        ("N", "Prefer not to say"),
    ]
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default="N")

    # non-active until app is extended in functionality.
    account_number = models.CharField(
        max_length=20, unique=True, blank=True, null=True
    )
    registration_date = models.DateTimeField(auto_now_add=True)

    # non-active until app is extended in functionality.
    payment_method = models.CharField(max_length=50, blank=True, null=True)

    # Keeping these set to true so that they allow them to be essentially empty
    # until the application has extended functionality of ordering in place.
    purchase_order_date = models.DateTimeField(null=True, blank=True)
    delivery_order_date = models.DateTimeField(null=True, blank=True)

    # non-active until app is extended in functionality.
    basket_item_count = models.IntegerField(default=0)

    # Both memorable name and memorable date can be used as security questions
    # if talking over the telephone.
    memorable_name = models.CharField(
        max_length=60, default="Your Memorable Name"
    )

    # Defines the accepted format of dates, when they are put in by the user.
    memorable_date = models.DateField(blank=True, null=True)

    # Links the CustomerAccount model to the django-allauth.
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # Returns the username.
    # Disabling pylint because the warning is a linter issue and distracting.
    def __str__(self):
        return self.user.username  # pylint: disable=no-member
