# Imports the required modules and models.
from django.contrib import admin
from .models import CustomerAccount


class CustomerAccountAdmin(admin.ModelAdmin):
    """
    CustomerAccountAdmin handles the customer account in the admin panel.
    """

    # Sets the fields that'll be displayed in the admin panel list view
    list_display = (
        "user",
        "phone",
        "address_line_1",
        "city",
        "county",
        "post_code",
        "registration_date",
    )
    # Sets which fields can be searched in the admin panel.
    search_fields = ("user__username", "phone", "city", "county", "post_code")

    # This defines the filter that the admin can filter by.
    # Including the filters of purchase_order_date and delivery_order_date
    # in the application but they'll only be utilized when functionality
    # is extended.
    list_filter = (
        "city",
        "county",
        "registration_date",
    )


# Using a decorator to ensure this is registered and displayed in the
# admin panel.
admin.site.register(CustomerAccount, CustomerAccountAdmin)
