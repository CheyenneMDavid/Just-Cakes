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
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .models import CustomerAccount
from .forms import CreateProfileForm

# from .forms import UpdateProfileForm  NOTE SORT OUT THE FORMS.PY & THE HTML


def customer_accounts_list(request):
    """
    The view fetches all the customer accounts from the database and renders
    them in a list view which only and admin will have access to.
    """
    # TODO: Implement features described in comments, for future development.


# Using the login_required decorator to ensure that access is restricted to
# only authenticated users.
@login_required
def customer_accounts_detail(request, id):
    """
    Shows the details of a single account.
    If it can't find it or it doesn't exist, it shows a 404 error.
    """
    account = get_object_or_404(CustomerAccount, id=id)

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
        "customer_accounts_detail.html",
        {"account": account, "customer_account": customer_account},
    )


# Using the login_required decorator to ensure that access is restricted to
# only authenticated users.
@login_required
def create_customer_profile(request):
    """
    This handles the customer signup process.
    If the method is POST, it validates the form data and either creates a new
    user or returns errors.
    If the method is GET, it renders the empty signup form.
    """
    # Checks if the incoming request is a post request. If it is, then we
    # execute this code block.  If it's not, then it's treated as a GET and
    # moves onto rendering the signup-form.
    if request.method == "POST":
        form = CreateProfileForm(request.POST)

        # If the the form's valid, the data's saved and a success message
        # is displayed to the user before they're redirected to the gallery of
        # available cakes.
        if form.is_valid():
            user = form.save(request)
            messages.success(
                request,
                "Account created successfully! You are now being logged in!",
            )
            login(request, user)

            # Redirects the user to the gallery of available cakes.
            return redirect("cake_list")
        else:
            # If form is not validated, the user receives an error message and
            # requested to try again.
            messages.error(
                request,
                "There was an error in your signup. "
                "Please check your details and try again.",
            )
    # else the request is treated as a GET, creating a new empty form instance.
    else:
        form = CreateProfileForm()

    # Render the signup page
    return render(
        request,
        "customer_accounts/create_customer_profile_form.html",
        {"form": form},
    )


# Using the login_required decorator to ensure that access is restricted to
# only authenticated users.
@login_required
def update_customer_profile(request, id):
    """
    This enables a customer to update their profile and gives them a success
    message when they've done it.
    """
    # Ensuring that the user is updating their own profile.
    if request.user.id != id:
        messages.error(
            request,
            "This is not your profile. You do not have permission to edit"
            "this profile.",
        )
        #
        #  ######  NOTE TO SELF  ##  Ask advice on where they should be
        # redirected to in this instance, or how it should be better dealt
        # with because at this point, anyone finding themselves here,
        # may have malicious intent.
        #
        # Redirect to a suitable page (perhaps the user's profile page or back
        # out to the gallery images.  )
        return redirect("customer_accounts_detail", id=request.user.id)

    # Retrieves a customer account that's linked to the user that's logged in.
    customer_account = get_object_or_404(CustomerAccount, id=id)

    # Checks if it's a post request
    if request.method == "POST":
        # If it is, then it's initialized with the data that will be used to
        # update the account.
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
    return render(request, "cake_list.html", {"form": form})


# Using the login_required decorator to ensure that access is restricted to
# only authenticated users.
@login_required
def confirm_delete_customer_profile(request, id):
    """
    Handles the confirmation of a request to delete
    """

    # Ensuring that the user is deleting their own profile.
    if request.user.id != id:
        messages.error(
            request,
            "This is not your profile. You do not have permission to delete it"
            "this profile.",
        )
        #
        #  ######  NOTE TO SELF  ##  Ask advice on where they should be
        # redirected to in this instance, or how it should be better dealt
        # with because at this point, anyone finding themselves here,
        # may have malicious intent.
        #
        # Redirect to a suitable page (perhaps the user's profile page or back
        # out to the gallery images.  )
        #
        #
        # REMEMBER to get advice on this and probably need to apply it right
        # across everything in this file!
        #
        return redirect("customer_accounts_detail", id=request.user.id)

    # Retrieve the CustomerAccount instance with the given ID or return a
    # 404 response if not found.
    customer_account = get_object_or_404(CustomerAccount, id=id)

    account_data_awaiting_deletion = {"customer_account": customer_account}

    # Renders a html page with a danger warning, a go back button and a button
    # to confirm deletion
    return render(
        request, "confirm_delete.html", account_data_awaiting_deletion
    )


# Using the login_required decorator to ensure that access is restricted to
# only authenticated users.
@login_required
def delete_customer_profile(request, id):
    """
    handles the deletion of a customer's profile
    """

    # Retrieve the CustomerAccount instance with the given ID or return a
    # 404 response if not found.
    customer_account = get_object_or_404(CustomerAccount, id=id)

    # Deletes the customer account/profile.
    customer_account.delete()

    # Confirms deletion message to user, using an f-string and the user's name
    messages.success(request, f"{customer_account.name} has been deleted.")

    # Returns user to the gallery of available cakes
    return redirect("{% url 'cake_list' %}")
