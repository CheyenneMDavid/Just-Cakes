from django.urls import path
from .views import (
    customer_account_detail,
    update_customer_account,
    confirm_delete_customer_account,
    delete_customer_account,
)

app_name = "customer_accounts"

urlpatterns = [
    path(
        "<int:pk>/", customer_account_detail, name="customer_account_detail"
    ),
    path(
        "<int:pk>/update/",
        update_customer_account,
        name="update_customer_account",
    ),
    path(
        "<int:pk>/confirm_delete/",
        confirm_delete_customer_account,
        name="confirm_delete_customer_account",
    ),
    path(
        "<int:pk>/delete/",
        delete_customer_account,
        name="delete_customer_account",
    ),
]
