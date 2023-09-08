from django.db import models
from django.contrib.auth.models import User


class CustomerAccount(models.Model):
    """
    Customer account model uses the allauth/django user model which extends
    the User model with additional fields.
    """

    # I've kept the character count pretty l because th is only dealing
    # with UK addresses, so 60 is more than long enough.
    # The longest town in the uk is in wales and only has 58 letters.
    phone = models.CharField(max_length=12)
    address_line_1 = models.CharField(max_length=50)
    address_line_2 = models.CharField(max_length=60)
    city = models.CharField(max_length=60)
    county = models.CharField(max_length=20)
    post_code = models.CharField(max_length=15)

    # non-active until app is extended in functionality.
    account_number = models.CharField(max_length=20, unique=True)
    registration_date = models.DateTimeField(auto_now_add=True)

    # non-active until app is extended in functionality.
    payment_method = models.CharField(max_length=50)

    # Keeping these set to true so that they allow them to be essentially empty
    # until the application has extended functionality of ordering in place.
    purchase_order_date = models.DateTimeField(null=True, blank=True)
    delivery_order_date = models.DateTimeField(null=True, blank=True)

    # non-active until app is extended in functionality.
    basket_item_count = models.IntegerField(default=0)

    # Links the CustomerAccount model to the django-allauth.
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # Returns the username.
    # Disabling pylint because the warning is a linter issue and distracting.
    def __str__(self):
        return self.user.username  # pylint: disable=no-member
