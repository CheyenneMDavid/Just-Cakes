from django import forms
from .models import Contact
from django.core.validators import RegexValidator


# Credit for this regex pattern is StackOverflow at this page:
# https://stackoverflow.com/questions/25155970/
# validating-uk-phone-number-regex-c
phone_regex = RegexValidator(
    regex=r"^(((\+44\s?\d{4}|\(?0\d{4}\)?)\s?\d{3}\s?\d{3})|"
    r"((\+44\s?\d{3}|\(?0\d{3}\)?)\s?\d{3}\s?\d{4})|"
    r"((\+44\s?\d{2}|\(?0\d{2}\)?)\s?\d{4}\s?\d{4}))(\s?\#(\d{4}|\d{3}))?$",
    message="Please enter a valid UK Phone number",
)


# Using the Contact model, defining the fields that will be used in the
# contact form.
class ContactForm(forms.ModelForm):

    phone_number = forms.CharField(validators=[phone_regex])

    class Meta:
        model = Contact
        fields = ["name", "email", "phone_number", "message"]
