"""
Signal handlers for creating CustomerAccount instances every time a new user
is registered.
"""

from django.db.models.signals import post_save
from django.contrib.auth import get_user_model
from django.dispatch import receiver
from .models import CustomerAccount

# Importing and using the "get_user_model" for flexibility and easier
# maintenance of the code in the future.
User = get_user_model()


@receiver(post_save, sender=User)
def create_customer_account(sender, instance, created, **kwargs):
    """
    Signal handler to create a CustomerAccount whenever a new User is created.
    Using **kwargs allows the function to handle extra,  keyword
    arguments in the future, guarding against potential errors during updates.
    """
    if created:
        CustomerAccount.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_customer_account(sender, instance, **kwargs):
    """
    Signal handler to save a CustomerAccount instance whenever a User
    instance is saved.  I'm including **kwargs to allow for any extra/new
    keyword arguments
    passed by the signal in the future which allows better flexibility in the
    future.
    """

    # Save the associated CustomerAccount when the User is saved.
    instance.customeraccount.save()
