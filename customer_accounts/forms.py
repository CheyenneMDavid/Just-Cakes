"""
Importing Django forms and CustomerAccount model to create forms based on
the model.

"""

from django import forms
from .models import CustomerAccount
import datetime


class UpdateProfileForm(forms.ModelForm):
    """
    Form for updating a customer's profile.
    It accepts date input in the format of dd.mm.yy and has validation to
    ensure the dates can't be in the future.
    """

    birth_date = forms.DateField(
        input_formats=["%d.%m.%Y"],
        required=False,
        help_text="Please enter your D.O.B. in dd.mm.yy format.",
    )
    memorable_date = forms.DateField(
        input_formats=["%d.%m.%Y"],
        required=False,
        help_text="Please enter a memorable date in dd.mm.yy format.",
    )

    class Meta:
        model = CustomerAccount
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

    def clean_birth_date(self):
        date = self.cleaned_data.get("birth_date")
        if date and date > datetime.date.today():
            raise forms.ValidationError(
                "Your D.O.B. can't be in the future!",
            )
        return date

    def clean_memorable_date(self):
        date = self.cleaned_data.get("memorable_date")
        if date and date > datetime.date.today():
            raise forms.ValidationError(
                "Your memorable date can't be in the future!",
            )
        return date
