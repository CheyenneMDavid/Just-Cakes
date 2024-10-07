from decimal import Decimal
from django.test import TestCase
from cakes.models import CakeCategory, IndividualCake
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


class TestIndividualCakeModel(TestCase):
    """
    Testing for the IndividualCake model.
    """

    def setUp(self):
        """
        Creating an instance for testing with valid data.
        """
        category = CakeCategory.objects.create(category="Testing Category")

        # Create an individual cake instance with a valid category
        self.individual_cake = IndividualCake.objects.create(
            description="No Actual Chocolate!",
            name="Choco Surprise!",
            category=category,  # Assign the category instance here
            number_of_layers=3,  # Ensure all required fields are provided
            price=Decimal("10.99"),
        )

    def test_individual_cake_creation(self):
        # Retrieve the created cake and check off it's values
        individual_cake = IndividualCake.objects.get(name="Choco Surprise!")
        self.assertEqual(individual_cake.description, "No Actual Chocolate!")
        self.assertEqual(individual_cake.number_of_layers, 3)
        # Ensuring to match decimal against decimal.
        self.assertEqual(individual_cake.price, Decimal("10.99"))
        self.assertFalse(individual_cake.is_gluten_free)
        self.assertFalse(individual_cake.is_plant_based)
        self.assertEqual(
            individual_cake.category.category, "Testing Category"
        )
