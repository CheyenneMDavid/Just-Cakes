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

# Moved the comments to the docstring at the top of the page to improve
# readability.
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import CustomerAccount
from .forms import UpdateProfileForm


def customer_accounts_list(request):
    """
    The view fetches all the customer accounts from the database and renders
    them in a list view which only and admin will have access to via a front
    end design, separate to what is currently available only via the django
    admin panel.
    """
    # TODO: Implement features described in comments, for future development.
    # Appropriate decorators will be assigned when this is fully implemented.


# Using the login_required decorator to ensure that access is restricted to
# only authenticated users.
# Changed from using id to using pk after coming across this in Stackoverflow
# here: https://stackoverflow.com/questions/2165865/django-queries-id-vs-pk
@login_required
def customer_account_detail(request, pk):
    """
    Shows the details of a single account.
    If it can't find it or it doesn't exist, it shows a 404 error.
    It uses a login_required decorator that checks if a user is
    logged in/authenticated.
    """

    # gets the customer account that's passed as an argument to
    # customer_account_detail
    account = get_object_or_404(CustomerAccount, pk=pk)

    # Tries to get the customer account that is associated with the user that
    # is currently logged in.
    try:
        customer_account = CustomerAccount.objects.get(user=request.user)

    # If there's no user account associated with the user that's currently
    # logged in, customer_account is set to None.
    except CustomerAccount.DoesNotExist:
        customer_account = None

    # Displays a customer_accounts detail page that is associated with the
    # user that is currently logged in.
    return render(
        request,
        "customer_accounts/customer_account_detail.html",
        {"account": account, "customer_account": customer_account},
    )


# Using the login_required decorator to ensure that access is restricted to
# only authenticated users.
@login_required
def update_customer_profile(request, pk):
    """
    This enables a customer to update their profile and gives them a success
    message when they've done it.
    """
    # Ensuring that the user is updating their own profile.
    if request.user.pk != pk:
        messages.error(
            request,
            "This is not your profile. You do not have permission to edit"
            "this profile.",
        )
        return redirect(
            "customer_account/customer_account_detail",
            pk=request.user.pk,
        )
    # Retrieves a customer account that's linked to the user that's logged in.
    customer_account = get_object_or_404(CustomerAccount, pk=pk)
    # Checks if it's a post request
    if request.method == "POST":
        form = UpdateProfileForm(request.POST, instance=customer_account)
        # Validates the form data
        if form.is_valid():
            # And then saves the updated customer_account.
            form.save()
            # Displays a message to the user, informing them of the successful
            # updating of their profile.
            messages.success(
                request,
                "Your profile has been updated. Remember, you can come back"
                "and update this anytime.",
            )
            # Redirects the user to the gallery of available cakes.
            return redirect("cake_list")
    # Otherwise, if it's a GET request, it gets the customer's account details.
    else:
        form = UpdateProfileForm(instance=customer_account)
    # Redirects the user to the gallery of available cakes.
    return render(
        request,
        "customer_accounts/customer_profile_update_form.html",
        {
            "form": form,
        },
    )


# Using the login_required decorator to ensure that access is restricted to
# only authenticated users.
@login_required
def confirm_delete_customer_profile(request, pk):
    """
    Handles the confirmation of a request to delete
    """
    # Ensuring that the user is deleting their own profile.
    if request.user.pk != pk:
        messages.error(
            request,
            "This is not your profile. You do not have permission to delete it"
            "this profile.",
        )
        return redirect("customer_account_detail", pk=request.user.pk)
    # Retrieve the CustomerAccount instance with the given ID or return a
    # 404 response if not found.
    customer_account = get_object_or_404(CustomerAccount, pk=pk)
    account_data_for_deletion = {"customer_account": customer_account}
    # Renders a html page with a danger warning, a go back button and a button
    # to confirm deletion
    return render(request, "confirm_delete.html", account_data_for_deletion)


# Using the login_required decorator to ensure that access is restricted to
# only authenticated users.
@login_required
def delete_customer_profile(request, pk):
    """
    handles the deletion of a customer's profile
    """
    # Retrieve the CustomerAccount instance with the given ID or return a
    # 404 response if not found.
    customer_account = get_object_or_404(CustomerAccount, pk=pk)
    # Deletes the customer account/profile.
    customer_account.delete()
    # Confirms deletion message to user, using an f-string and the user's name
    messages.success(request, f"{customer_account.name} has been deleted.")
    # Returns user to the gallery of available cakes
    return redirect("account/account_signup")
