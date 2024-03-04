from django.contrib import admin
from .models import Contact


# Registering the Contact model with the admin interface
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    """
    Defines the fields to be used in admin panel with a filter of date the
    record was created.
    """

    list_display = ("name", "email", "phone_number", "created_at")
    list_filter = ("created_at",)
