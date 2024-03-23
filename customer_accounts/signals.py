"""
Signal handlers for creating, updating and deleting the CustomerAccount
instances.
"""

from django.db.models.signals import post_save, post_delete
from django.contrib.auth import get_user_model
from django.dispatch import receiver
from .models import CustomerAccount

User = get_user_model()


@receiver(post_save, sender=User)
def create_or_update_customer_account(sender, instance, created, **kwargs):
    """
     Signal handler to create or update a CustomerAccount whenever a User is
    created or updated.  Less code/more streamline than having them as
    separate functions and less potential for glitches due to two functions
    doing a very similar task.
    Here, it checks if the user instance is newly created.  If it is, then a
    new customer account instance is created and associated with the new user
    instance.
    Otherwise the customer account is instance is saved with the new
    information.
    """
    if created:
        CustomerAccount.objects.create(user=instance)
    else:
        instance.customeraccount.save()


@receiver(post_delete, sender=CustomerAccount)
def delete_related_user(sender, instance, **kwargs):
    """
    Signal handler to ensure that user is also deleted when the customer
    account is deleted. "Gracefully" handling the deletion of a user with the
    use of a try/except block.  This way, if there's not an associated user,
    nothing else needs to happen.
    """
    try:
        user = instance.user
        user.delete()
    except User.DoesNotExist:
        pass
