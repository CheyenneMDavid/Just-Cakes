from django.test import TestCase
from cakes.models import CakeCategory


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
