# Import required modules
from django.db import models


# -- This section of the cake models deal with the attributes of the cakes
# These models are for describing the cakes according to type (i.e. wedding,
# novelty, birthday), flavours, colours, layers, diet, allergies and price.
class CakeType(models.Model):
    """
    Represents the type fo cake.
    """

    # Max length set to 100 to accommodate longer names in the future.
    type = models.CharField(max_length=100)

    # Specifying retruning a string to offset linter warnings
    def __str__(self):
        return str(self.type)


class CakeFlavour(models.Model):
    """
    Represents the cake flavours available.
    """

    flavour = models.CharField(max_length=50)

    # specifying retruning a string to offset linter warnings
    def __str__(self):
        return str(self.flavour)


class CakeColour(models.Model):
    """
    Represents the cake flavours available.
    """

    colour = models.CharField(max_length=100)

    # specifying retruning a string to offset linter warnings
    def __str__(self):
        return str(self.colour)


class IndividualCake(models.Model):
    """
    "IndividualCake", brings all the attributes together in it's representation
    as one cake and the name that is attributed to it.
    """

    # Name of the cake. Max length set to 100 to accommodate longer names
    # in the future.
    name = models.CharField(max_length=100)

    # Foreign key to CakeType. If a CakeType is deleted, all associated
    # cakes will also be deleted (CASCADE).
    type = models.ForeignKey(CakeType, on_delete=models.CASCADE)

    # Indicates if the cake is gluten free and using the statement " is "
    # so that it can be marked as Tue or False.
    is_gluten_free = models.BooleanField()

    # Indicates if the cake is plant based and using the statement " is "
    # so that it can be marked as Tue or False.
    is_plant_based = models.BooleanField()

    # Number of layers the cake has.
    number_of_layers = models.IntegerField()

    # Price of the cake. 5 digits allowing for a max price of 999.99.
    price = models.DecimalField(max_digits=5, decimal_places=2)

    # Many-to-Many relation as a cake can have multiple flavours.
    flavours = models.ManyToManyField(CakeFlavour)

    #
