"""
I've chosen to import individual objects rather than the views module as a
whole, for better readability and less chance of mixing things up, for myself
if nobody else.
I've defined the URL patterns for 'customer_accounts' in Django.
"""
# Django imports
from django.urls import path
from .forms import UpdateProfileForm

# Local imports: forms and views specific to the customer_accounts application
from .views import (
    customer_accounts_list,
    customer_accounts_detail,
    update_customer_profile,
    confirm_delete_customer_profile,
    delete_customer_profile,
)

# URL patterns for the customer accounts application.
urlpatterns = [
    path("", customer_accounts_list, name="customer_accounts_list"),
    path(
        "<int:pk>/", customer_accounts_detail, name="customer_accounts_detail"
    ),
    path(
        "<int:pk>/update/",
        update_customer_profile,
        name="update_customer_profile",
    ),
    path(
        "<int:pk>/confirm_delete/",
        confirm_delete_customer_profile,
        name="confirm_delete_customer_profile",
    ),
    path(
        "<int:pk>/delete/",
        delete_customer_profile,
        name="delete_customer_profile",
    ),
]