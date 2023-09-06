# Import required modules
from django.db import models


class CakeType(models.Model):
    """
    Representing type of cake.
    """

    # Max length set to 100 to accommodate longer names in the future.
    type = models.CharField(max_length=100)

    # specifying retruning a string to offset linter warnings
    def __str__(self):
        return str(self.type)


class Flavour(models.Model):
    """
    Cake flavours
    """

    flavour = models.CharField(max_length=50)

    # specifying retruning a string to offset linter warnings
    def __str__(self):
        return str(self.flavour)


class Colour(models.Model):
    """
    Colours of the cakes.
    """

    colour = models.CharField(max_length=100)

    # specifying retruning a string to offset linter warnings
    def __str__(self):
        return str(self.colour)


class Cake(models.Model):
    """
    Represents the cakes, along with their names, types, gluten-free or plant-based status,
    number of layers, prices, flavours, and colours.
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
    flavours = models.ManyToManyField(Flavour)
