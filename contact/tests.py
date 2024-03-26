from django.test import TestCase
from .forms import ContactForm


class ContactFormTests(TestCase):
    """
    Tests for contact form submission
    """

    def test_form_is_valid(self):
        # Contact form with valid input.
        form_data = {
            "name": "Bob Smith",
            "email": "bob@email.com",
            "phone_number": "01773667668",
            "message": "Generic content of message",
        }

        form = ContactForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_form_is_invalid(self):
        # Contact form with invalid input.
        form_data = {
            "name": "6428uh#",
            "email": "e5b68",
            "phone_number": "w476v",
            "message": "",  # message field is left empty.
        }
        form = ContactForm(data=form_data)
        self.assertFalse(form.is_valid())
