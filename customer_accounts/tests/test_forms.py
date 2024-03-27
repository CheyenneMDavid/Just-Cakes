from django.test import TestCase
from customer_accounts.forms import UpdateProfileForm


class UpdateProfileFormTest(TestCase):
    """
    Test cases for the UpdateProfileForm class.
    """

    def test_valid_form(self):
        """
        Test if the form is valid with valid form data.
        """
        form_data = {
            "first_name": "John",
            "last_name": "Doe",
            "phone": "01227731623",
            "address_line_1": "123 This Rd",
            "address_line_2": "Town name",
            "city": "Any City",
            "county": "Any County",
            "post_code": "en5 8td",
            "birth_date": "1990-01-01",
            "gender": "N",
            "memorable_name": "My Dog",
            "memorable_date": "2010-01-01",
        }
        form = UpdateProfileForm(data=form_data)
        print(form.errors)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        """
        Test if the form is invalid with invalid form data.
        """
        form_data = {
            "first_name": "3w4567vgb%",
            "last_name": "~#",
            "phone": "Arnold",
            "address_line_1": "--+=",
            "address_line_2": "Town name",
            "city": "Any City",
            "county": "Any County",
            "post_code": "12345",
            "birth_date": "Not a Date",
            "gender": "x",
            "memorable_name": "(^&(*^))",
            "memorable_date": "Not a Date",
        }

        form = UpdateProfileForm(data=form_data)
        print(form.errors)
        self.assertFalse(form.is_valid())

    def test_blank_data(self):
        """
        Test if the form is valid with blank data.
        """
        form = UpdateProfileForm(data={})
        self.assertTrue(form.is_valid())
