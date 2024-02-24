"""
This models.py is for managing all the data for the cakes app.
Category, flavours, names and the individual descriptions, none of which are 
hardcoded, leaving a site admin free to create and add new ones.
"""

from django.db import models
from cloudinary.models import CloudinaryField


class CakeCategory(models.Model):
    """
    Representing the category for cakes
    """

    category = models.CharField(max_length=100, default="to be set")

    def __str__(self):
        return str(self.category)


class CakeFlavour(models.Model):
    flavour = models.CharField(max_length=50)

    def __str__(self):

        return str(self.flavour)


class CakeColor(models.Model):
    color = models.CharField(max_length=50)

    def __str__(self):
        return str(self.color)


class IndividualCake(models.Model):
    description = models.TextField(default="")

    def __str__(self):
        return str(self.name)

    name = models.CharField(max_length=100)

    category = models.ForeignKey(
        CakeCategory,
        on_delete=models.PROTECT,
        default=None,
    )

    is_gluten_free = models.BooleanField()

    is_plant_based = models.BooleanField()

    number_of_layers = models.IntegerField()

    price = models.DecimalField(max_digits=5, decimal_places=2)

    flavours = models.ManyToManyField(CakeFlavour)


# Used for displaying specific cake images when they're setup via the admin
# screen.
class CakeImage(models.Model):
    cake = models.ForeignKey(
        IndividualCake, related_name="images", on_delete=models.CASCADE
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
