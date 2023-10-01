"""
Views for the Customer Accounts app.
It contains the views for rendering the customer accounts lists and details.
It also handles the customer's signups.
It uses Django's built-in functions and methods for managing HTTP
requests, rendering templates, and performing actions like login and
redirecting the users.
"""
# Using messages module to provide users with messages of successful or
# unsuccessful signups.
from django.contrib import messages

# render to return a template/page, get_object_or_404 to return a 404
# response if an object isn't found. And redirect to take a user somewhere
# after they have completed a task.  Example being, the home page after
# signing in.
from django.shortcuts import render, get_object_or_404, redirect


from django.contrib.auth import login

# Importing the login_required decorator to restrict access of accounts to
# authenticated users.
from django.contrib.auth.decorators import login_required

# Importing CustomerAccount model.
from .models import CustomerAccount

# Importing the CustomerProfileForm.
from .forms import CustomerProfileForm


# This function will only be available to someone who is signed in as an
# admin and will include a decorator and the permission checks for it.
# It's planned for future functionality and the logic within it will be
# replaced with a "pass" and a "TODO" comment as the function is planned for
# future functionality.
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

    # Displays a customer_account-s detail page that is associated with the
    # user that is currently logged in.
    return render(
        request,
        "customer_accounts_detail.html",
        {"account": account, "customer_account": customer_account},
    )


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
        form = CustomerProfileForm(request.POST)

        # If the the form's valid, the data's saved and a success message
        # is displayed to the user before they're redirected to the homepage.
        if form.is_valid():
            user = form.save(request)
            messages.success(
                request,
                "Account created successfully! You are now being logged in!",
            )
            login(request, user)

            # Using the imported "HomePageView" in the urls.py and the
            # imported "redirect" shortcut.
            return redirect("home")
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
        form = CustomerProfileForm()

    # Render the signup page
    return render(
        request,
        "customer_accounts/create_customer_profile_form.html",
        {"form": form},
    )
