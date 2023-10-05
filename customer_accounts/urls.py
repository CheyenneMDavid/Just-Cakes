"""Importing objects"""
# I've chosen to import individual objects rather than the views module as a
# whole, for better readability and less chance of mixing things up.
from django.urls import path
from .views import (
    customer_accounts_list,
    customer_accounts_detail,
    create_customer_profile,
    update_customer_profile,
    confirm_delete_customer_profile,
    delete_customer_profile,
)


# URL patterns for the customer accounts application.
urlpatterns = [
    path("", customer_accounts_list, name="customer_accounts_list"),
    path(
        "<int:id>/", customer_accounts_detail, name="customer_accounts_detail"
    ),
    path(
        "create-profile/",
        create_customer_profile,
        name="create_customer_profile",
    ),
    path(
        "update/<int:id>/",
        update_customer_profile,
        name="update_profile",
    ),
    path(
        "confirm_delete/<int:id>/",
        confirm_delete_customer_profile,
        name="confirm_delete_profile",
    ),
    path("delete/<int:id>/", delete_customer_profile, name="delete_profile"),
]
