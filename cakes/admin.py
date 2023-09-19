# Imports the required modules and classes
from django.contrib import admin

from .models import (
    CakeType,
    CakeFlavour,
    CakeColor,
    IndividualCake,
    CakeImage,
)


# This section of the cake models deal with the attributes of the cakes
# These models are for describing the cakes according to type (i.e. wedding,
# novelty, birthday), flavours, colors, layers, diet, allergies and price.


# In each class, I'm using the "@" to apply it as a decorator and register
# it in the admin panel where it can be managed.
@admin.register(CakeType)
class CakeTypeAdmin(admin.ModelAdmin):
    """
    Sets how CakeType appears and can be searched in the admin panel.
    """

    # Setting the fields that will be displayed in the admin panel's list view.
    list_display = ("type",)

    # Defining which fields can be searched using the admin panel's search bar.
    search_fields = ("type",)


# Decorator to register it in the admin panel.
@admin.register(CakeFlavour)
class CakeFlavourAdmin(admin.ModelAdmin):
    """
    Sets how the CakeFlavour appears and can be searched in the admin panel.
    """

    # Sets the fields that will be displayed in the admin panel's list view.
    list_display = ("flavour",)

    # Defining which fields can be searched using the admin panel's search bar.
    search_fields = ("flavour",)


# Decorator to register it in the admin panel.
@admin.register(CakeColor)
class CakeColorAdmin(admin.ModelAdmin):
    """
    Sets how Cakecolor appears and can be searched in the admin panel.
    """

    # Sets the fields that will be displayed in the admin panel's list view.
    list_display = ("color",)

    # Defining which fields can be searched using the admin panel's search bar.
    search_fields = ("color",)


# Decorator to register it in the admin panel.
@admin.register(IndividualCake)
class IndividualCakeAdmin(admin.ModelAdmin):
    """
    Sets how IndividualCake appears and can be managed in the admin panel.
    """

    # Sets the fields that will be displayed in the admin panel's list view.
    list_display = (
        "name",
        "type",
        "is_gluten_free",
        "is_plant_based",
        "number_of_layers",
        "price",
        "description",
    )

    # Defining which fields can be searched using the admin panel's search bar.
    # Using "__" to search for CakeType by the cake's name and description.
    search_fields = ("name", "type__type", "description")

    # Adds options in the admin panel for filtering.
    list_filter = ("type", "is_gluten_free", "is_plant_based")


@admin.register(CakeImage)
class CakeImageAdmin(admin.ModelAdmin):
    """
    Sets how CakeImage appears and can be searched in the admin panel.
    """

    # Defining which fields can be searched using the admin panel's search bar.
    list_display = (
        "cake",
        "image",
    )
    # Defining which fields can be searched using the admin panel's search bar.
    # Using "__" to search for CakeImage by the cake's name.
    search_fields = ("cake__name",)
