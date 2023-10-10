"""
Importing Django forms and CustomerAccount model to create forms based on
the model.

"""
from django import forms
from .models import CustomerAccount


class UpdateProfileForm(forms.ModelForm):
    """
    Form for updating a customer's profile.
    """

    class Meta:
        model = CustomerAccount
        # fields that a user is able to update.
        fields = [
            "first_name",
            "last_name",
            "phone",
            "address_line_1",
            "address_line_2",
            "city",
            "county",
            "post_code",
            "birth_date",
            "gender",
            "memorable_name",
            "memorable_date",
        ]
