# Imports the required modules and models.
from django.contrib import admin
from .models import CustomerAccount


class CustomerAccountAdmin(admin.ModelAdmin):
    """
    Defines the admin interface for CustomerAccount models.
    This configuration improves admin interactions by allowing
    sorting, searching, and filtering based on relevant fields.
    """

    # Fields to display in the admin panel list view, gives the admin a quick view of important information.
    list_display = (
        "user",
        "first_name",
        "last_name",
        "phone",
        "city",
        "county",
        "post_code",
        "registration_date",
    )

    # Fields that can be used to search through CustomerAccounts in the admin
    # panel.
    search_fields = (
        "user__username",
        "first_name",
        "last_name",
        "phone",
        "post_code",
    )

    # Sets the default ordering for CustomerAccounts in the admin list view;
    # earliest registration dates first.
    ordering = ("registration_date",)

    # Fields available for filtering in the admin panel, aiding in efficient
    # navigation and management of records.
    list_filter = (
        "last_name",
        "phone",
        "city",
        "county",
        "registration_date",
    )


# Registers the CustomerAccountAdmin with the associated model to ensure it's
# available in the Django admin panel.
admin.site.register(CustomerAccount, CustomerAccountAdmin)
