"""
Import necessary modules and functions from Django for handling signals,
user models and models.
"""
# user models, and models.
from django.db.models.signals import post_save
from django.contrib.auth import get_user_model
from django.dispatch import receiver
from .models import CustomerAccount

# Importing and using the "get_user_model" for flexibility and easier
# maintenance of the code in the future.
User = get_user_model()


# Signal handler to create a CustomerAccount whenever a new User is created.
# Using **kwargs allows the function to handle extra,  keyword
# arguments in the future, guarding against potential errors during updates.
@receiver(post_save, sender=User)
def create_customer_account(sender, instance, created, **kwargs):
    """
    Signal handler to create a CustomerAccount when a new User is created.

    Args:
        instance: The User instance being saved.
        created: A boolean indicating if the User was just created.
        kwargs: Additional keyword arguments, to stave off unwanted errors.
    Returns:
        None in simple terms.
    """
    if created:
        CustomerAccount.objects.create(user=instance)


# Signal handler to save a CustomerAccount whenever a User is saved.
# Using **kwargs allows the function to handle extra,  keyword
# arguments in the future, guarding against potential errors during updates.
@receiver(post_save, sender=User)
def save_customer_account(sender, instance, **kwargs):
    """
    Signal handler to save a CustomerAccount when a User is saved.

    Args:
        instance: The User instance being saved.
        kwargs: Additional keyword arguments, to stave off unwanted errors.

    Returns:
        None in simple terms.
    """
    # Save the associated CustomerAccount when the User is saved.
    instance.customeraccount.save()
