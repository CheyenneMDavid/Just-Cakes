"""
This models.py is for managing all the data for the cakes app.
Category, flavours, names and the individual descriptions, none of which are
hardcoded, leaving a site admin free to create and add new ones.
"""

from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from cloudinary.models import CloudinaryField


class CakeCategory(models.Model):
    """
    Representing the category for cakes. It allows for additional categories
    to be added.
    """

    category = models.CharField(
        max_length=100,
        unique=True,
        default="to be set",
    )

    def __str__(self):
        return str(self.category)


class IndividualCake(models.Model):
    """
    A model representing an individual cake, which belongs to a category. The
    category being the foreign key, so given the the attribute of PROTECT when
    an individual cake is deleted.
    """

    description = models.TextField(default="")
    name = models.CharField(max_length=100, unique=True)
    category = models.ForeignKey(
        CakeCategory,
        on_delete=models.PROTECT,
    )
    is_gluten_free = models.BooleanField(default=False)
    is_plant_based = models.BooleanField(default=False)

    # Guidance on how to limit the input was taken from stackoverflow here:
    # https://stackoverflow.com/questions/849142/how-to-limit-the-maximum-value-of-a-numeric-field-in-a-django-model
    # and whilst it's not solution with the most ratings from the page's
    # contributors, it is the solution that fitted the fields in my model.
    number_of_layers = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name


# Used for displaying specific cake images when they're setup via the admin
# screen.
class CakeImage(models.Model):
    cake = models.ForeignKey(
        IndividualCake,
        related_name="images",
        on_delete=models.SET_NULL,
        null=True,
    )
    image = CloudinaryField("image", folder="just_cakes_images")

    def __str__(self):
        return f"{self.cake.name} Image"


# Used to ensure an image is displayed in case the admin doesn't supply an
# image for an addition to the gallery.
class Cake(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    # Used in the conditional logic in the index,html which is the gallery of
    # cake images.
    default_image = models.URLField(default="placeholder")
