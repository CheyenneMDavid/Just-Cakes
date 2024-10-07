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

    name = models.CharField(
        max_length=100, help_text="Please enter your name"
    )
    email = models.EmailField(help_text="Please enter a valid email address")
    phone_number = models.CharField(
        max_length=20, help_text="Please enter a valid phone number"
    )
    message = models.TextField(
        help_text="Please leave your message here"
    )  # Corrected line
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """
        Returns a string representation of the Contact object.
        """
        return self.name
