from django import forms
from .models import Contact


# Using the Contact model, defining the fields that will be used in the
# contact form.
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ["name", "email", "phone_number", "message"]
