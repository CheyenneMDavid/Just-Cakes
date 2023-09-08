#  Imports the required modules
from django.urls import path
from . import views

# I've used the Code Institute walkthrough project of Hello Django as
# a template to follow when creating this file.

# URL patterns for the reviews application.
urlpatterns = [
    path(
        "customer_accounts/",
        views.customer_accounts_list,
        name="customer_account_list",
    ),
    path(
        "customer_accounts/<int:id>/",
        views.customer_accounts_detail,
        name="customer_account_detail",
    ),
]
