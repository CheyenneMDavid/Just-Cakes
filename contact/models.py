"""
Purpose of this model is to define the structure for storing information from
contact form submissions
"""

from django.db import models


class Contact(models.Model):
    """
    Fields being stored:
    name, email, phone number and a message.
    With a time stamp of when the  record was created.

    """

    name = models.CharField(max_length=100, verbose_name="Name")
    email = models.EmailField(verbose_name="Email")
    phone_number = models.CharField(max_length=20, verbose_name="Phone number")
    message = models.TextField(verbose_name="Message")
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Created at",
    )

    def __str__(self):
        """
        Returns a string representation of the Contact object.
        """
        return self.name
