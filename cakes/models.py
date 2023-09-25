# Import required modules
from django.db import models
from cloudinary.models import CloudinaryField


# This section of the cake models deal with the attributes of the cakes
# These models are for describing the cakes according to their category
# (i.e. wedding, novelty, birthday), flavours, colors, layers, diet, allergies
# and price.
class CakeCategory(models.Model):
    """
    Represents the cake category.
    """

    # Max length set to 100 to accommodate longer names in the future.
    # The 'default' parameter is set to "to be set" so it's clear that the
    # category should be defined when creating a new cake object.
    category = models.CharField(max_length=100, default="to be set")

    # Specifying returning a string to offset linter warnings
    # Using __str__ so the objects show correctly in the admin panel
    def __str__(self):
        return str(self.category)


class CakeFlavour(models.Model):
    """
    Represents the cake flavours available.
    """

    # flavour, using a max of 50 characters
    flavour = models.CharField(max_length=50)

    # Specifying returning a string to offset linter warnings
    # Using __str__ so the objects show correctly in the admin panel
    def __str__(self):
        return str(self.flavour)


class CakeColor(models.Model):
    """
    Represents the cake colors available.
    """

    color = models.CharField(max_length=50)

    # Specifying returning a string to offset linter warnings
    # Using __str__ so the objects show correctly in the admin panel
    def __str__(self):
        return str(self.color)


class IndividualCake(models.Model):
    """
    "IndividualCake", brings all the attributes together in it's representation
    as one cake and the name that is attributed to it.
    """

    # No limit on character count to ensure room for full descriptions.
    description = models.TextField(default="")

    # Specifying returning a string to offset linter warnings
    # Using __str__ so the objects show correctly in the admin panel
    def __str__(self):
        return str(self.name)

    # Name of the cake. Max length set to 100 to accommodate longer names
    # in the future.
    name = models.CharField(max_length=100)

    # Foreign key to CakeCategory. If a CakeCategory is deleted, django
    # checks to see if any other cake is reliant on cake category. If there
    # is, then it's protected from being deleted.
    category = models.ForeignKey(
        CakeCategory, on_delete=models.PROTECT, default=None
    )

    # Indicates if the cake is gluten free and using the statement " is "
    # so that it can be marked as True or False.
    is_gluten_free = models.BooleanField()

    # Indicates if the cake is plant based and using the statement " is "
    # so that it can be marked as True or False.
    is_plant_based = models.BooleanField()

    # Number of layers the cake has.
    number_of_layers = models.IntegerField()

    # Price of the cake. 5 digits allowing for a max price of 999.99.
    price = models.DecimalField(max_digits=5, decimal_places=2)

    # Many-to-Many relation as a cake can have multiple flavours.
    flavours = models.ManyToManyField(CakeFlavour)


# This section of the cake models deals with the images of cakes that are
# stored on cloudinary.
# Rather than just putting an extra line or so into the
# previous model in order to deal with the images, this is a totally separate
# model which will for multiple images of the same cake, which is likely given
# the nature of the site.
# Currently, there's only one image per cake.  But having a separate model
# makes it easier to manage this change in the future.


class CakeImage(models.Model):
    """
    For the moment, there's only one picture per cake. But it's likely that
    multiple angles of view for each cake will be added in the future.

    """

    # Cake is a foreign key for each cake.  It allows for a  many to many
    # relationship which will ultimately be the multiple photos of one cake.
    # Using CASCADE for deleting ensures that when a particular cake is no
    # longer being sold and is deleted, all other associated images will also
    # be deleted. Everything associated with that cake will also be deleted.
    cake = models.ForeignKey(
        IndividualCake, related_name="images", on_delete=models.CASCADE
    )

    # "image", because it's literally the image that's being stored on
    # cloudinary, using a specific folder "just_cakes_images"
    image = CloudinaryField("image", folder="just_cakes_images")

    # Using string literal to return the name of the cake as it's stored
    # on cloudinary and the word "image"
    def __str__(self):
        return f"{self.cake.name} Image"
