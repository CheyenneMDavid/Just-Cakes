"""Importing required modules for URL configuration and views"""
from django.urls import path
from .views import (
    customer_accounts_list,
    customer_accounts_detail,
    customer_signup,
)

# I've used the Code Institute walkthrough project of Hello Django as
# a template to follow when creating this file.

# URL patterns for the customer accounts application.
urlpatterns = [
    path("", customer_accounts_list, name="customer_account_list"),
    path(
        "<int:id>/", customer_accounts_detail, name="customer_account_detail"
    ),
    path("signup/", customer_signup, name="customer_signup"),
]
