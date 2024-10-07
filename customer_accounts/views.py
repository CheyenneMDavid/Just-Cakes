"""
Views for the Customer Accounts app.
This module manages the rendering of the customer accounts, lists and details.
It also manages the process of creating and updating a customer's profile.

It imports and uses the following modules and functions:
- messages: Feedback to users after successful and unsuccessful sign ins.
- render: Returns pages/templates.
- get_object_or_404: Returns a 404 response if an object isn't found.
- login: Logs users in after authentication and before re-direct.
- redirect: Navigates users to another page after a task is completed.
- login_required decorator: Restricts access by authenticated users.
- CustomerAccount model: Interact with the corresponding database.
- CreateProfileForm: Profile creation.
- UpdateProfileForm: Updating of profile.
"""

from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import CustomerAccount
from .forms import UpdateProfileForm


# Using the login_required decorator to ensure that access is restricted to
# only authenticated users.
@login_required
def customer_account_detail(request, pk):
    account = get_object_or_404(CustomerAccount, pk=pk, user=request.user)
    return render(
        request,
        "customer_accounts/customer_account_detail.html",
        {"account": account},
    )


# Using the login_required decorator to ensure that access is restricted to
# only authenticated users.
@login_required
def update_customer_account(request, pk):
    customer_account = get_object_or_404(
        CustomerAccount,
        pk=pk,
        user=request.user,
    )

    if request.method == "POST":
        form = UpdateProfileForm(request.POST, instance=customer_account)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                "Your profile has been updated successfully.",
            )
            return redirect(
                "customer_accounts:customer_account_detail", pk=pk
            )
    else:
        form = UpdateProfileForm(instance=customer_account)

    return render(
        request,
        "customer_accounts/customer_account_update_form.html",
        {
            "form": form,
        },
    )


# Using the login_required decorator to ensure that access is restricted to
# authenticated users.
@login_required
def confirm_delete_customer_account(request, pk):
    # Retrieves the customer account to be deleted.
    account = get_object_or_404(CustomerAccount, pk=pk, user=request.user)

    # Checks if the request method is POST, indicating the user has confirmed
    # deletion.
    if request.method == "POST":
        # Delete the customer account.
        account.delete()
        # Display a success message to the user.
        messages.success(
            request,
            "Your account has been successfully deleted.",
        )
        # Redirect the user to the sign-in page after deletion.
        return redirect("account_login")

    # If the request method is GET, then render the confirmation template
    # without deleting anything.
    return render(
        request,
        "customer_accounts/customer_account_confirm_deletion.html",
        {"account": account},
    )


# Using the login_required decorator to ensure that access is restricted to
# only authenticated users.
@login_required
def delete_customer_account(request, pk):

    customer_account = get_object_or_404(CustomerAccount, pk=pk)
    if request.user != customer_account.user:
        messages.error(
            request,
            "You do not have permission to delete this account.",
        )
        return redirect("customer_accounts:customer_account_detail", pk=pk)

    customer_account.delete()
    messages.success(request, "Your account has been successfully deleted.")

    return redirect("account/account_signup")
