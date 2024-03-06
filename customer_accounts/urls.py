# Django imports
from django.urls import path

# Imports of the forms and views needed for the customer accounts
from .views import (
    customer_account_detail,
    update_customer_profile,
    confirm_delete_customer_profile,
    delete_customer_profile,
)

# URL patterns for the customer accounts application.
urlpatterns = [
    # Viewing details for a particular profile.
    path("<int:pk>/", customer_account_detail, name="customer_account_detail"),
    path(
        "<int:pk>/update/",
        update_customer_profile,
        name="update_customer_profile",
    ),
    # Displays a confirmation page before deleting a profile
    path(
        "<int:pk>/confirm_delete/",
        confirm_delete_customer_profile,
        name="confirm_delete_customer_profile",
    ),
    # Page for deleting the profile.
    path(
        "<int:pk>/delete/",
        delete_customer_profile,
        name="delete_customer_profile",
    ),
    path(
        "update-profile/",
        update_customer_profile,
        name="update_profile",
    ),
]
