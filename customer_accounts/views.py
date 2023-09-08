from django.shortcuts import render, get_object_or_404
from .models import CustomerAccount


# I've used the Code Institute walkthrough project of Hello Django as
# a template to follow when creating this file.


def customer_accounts_list(request):
    """
    The view fetches all the customer accounts from the database and renders
    them in a list view.
    """
    accounts = CustomerAccount.objects.all()  # pylint: disable=no-member

    # Returns the customer_account_list.html
    return render(
        request, "customer_account_list.html", {"accounts": accounts}
    )


def customer_accounts_detail(request, id):
    """
    Shows the details of a single account.
    If it can't find it or it doesn't exist, it shows a 404 error.
    """
    account = get_object_or_404(CustomerAccount, id=id)

    # Returns the customer_account_list.html
    return render(
        request, "customer_account_detail.html", {"account": account}
    )
