"""
I was continually receiving errors from pylint saying that the "imports"
should all have docstrings. I don't recall being taught to include them
for imports but am choosing to heed to warning from the linter and
including them.
"""
from django.db.models.signals import post_save
from django.contrib.auth import get_user_model
from django.dispatch import receiver
from .models import CustomerAccount

# Importing and using "get_user_model" to allow flexibility and easier
# maintenance of the code in the future.
User = get_user_model()


@receiver(post_save, sender=User)
def create_customer_account(instance, created, **kwargs):
    """
    Signal handler to create a CustomerAccount when a new User is created.

    Args:
        instance: The User instance being saved.
        created: A boolean indicating if the User was just created.
        kwargs: Additional keyword arguments.

    Returns:
        None in simple terms.
    """
    if created:
        CustomerAccount.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_customer_account(instance, **kwargs):
    """
    Signal handler to save a CustomerAccount when a User is saved.

    Args:
        instance: The User instance being saved.
        kwargs: Additional keyword arguments.

    Returns:
        None in simple terms.
    """
    instance.customeraccount.save()
