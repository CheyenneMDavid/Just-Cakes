from django.test import TestCase
from cakes.models import CakeCategory
from django.core.exceptions import ValidationError


class CakeCategoryModelTests(TestCase):
    """
    Test cases for the CakeCategory model.
    """

    def test_cake_category_creation(self):
        """
        Test creating a CakeCategory instance.
        """
        # Creating a CakeCategory instance with the category "Wedding".
        category = CakeCategory.objects.create(category="Wedding")

        # Asserting that the category attribute of the created instance is
        # "Wedding".
        self.assertEqual(
            category.category,
            "Wedding",
            msg="Category should be wedding.",
        )

    def test_create_cake_category_without_name(self):
        """
        Testing the creation of a CakeCategory without providing an actual
        name for the instance.
        """
        # Trying to create a CakeCategory without providing an actual name for
        # the category should raise a validation error.
        category = CakeCategory()
        with self.assertRaises(ValidationError):
            # Called "full_clean" method on the "category" field, because the
            # conventional blank and null settings failed to enforce the
            # required validation.
            category.full_clean()
