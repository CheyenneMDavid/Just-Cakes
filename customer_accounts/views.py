"""
Views for the Customer Accounts app.
It contains the views for rendering the customer accounts lists and details.
It also handles the customer's signups.
It uses Django's built-in functions and methods for managing HTTP
requests, rendering templates, and performing actions like login and
redirecting the users.
"""
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login
from .models import CustomerAccount
from .forms import CustomSignupForm


def customer_accounts_list(request):
    """
    The view fetches all the customer accounts from the database and renders
    them in a list view.
    """
    accounts = CustomerAccount.objects.all()

    # Returns the customer_account_list.html
    return render(
        request, "customer_account_list.html", {"accounts": accounts}
    )


def customer_accounts_detail(request, id):
    """
    Shows the details of a single account.
    If it can't find it or it doesn't exist, it shows a 404 error.
    """
    # The get_object_or_404 function tries to get a CustomerAccount object.
    # If the object's found, it’s assigned to the variable “account”.
    # If not, then a HTTP 404 response is returned.
    account = get_object_or_404(CustomerAccount, id=id)

    # Returns the customer_account_detail.html
    return render(
        request, "customer_account_detail.html", {"account": account}
    )


def customer_signup(request):
    """
    This handles the customer signup process.
    If the method is POST, it validates the form data and either creates a new
    user or returns errors.
    If the method is GET, it renders the empty signup form.
    """
    # Checks if the incoming request is a post request. If it is, then we
    # execute this code block.  If it's not, then it;s treated as a GET and
    # moves onto rendering the signup-form.
    if request.method == "POST":
        form = CustomSignupForm(request.POST)

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
                "There was an error in your signup. Please check your details"
                "and try again.",
            )
    # else the request is treated as a GET, creating a new empty form instance.
    else:
        form = CustomSignupForm()

    # Render the signup page
    return render(
        request, "customer_accounts/customer_signup_form.html", {"form": form}
    )
