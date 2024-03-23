"""
Purpose of this view is to handle the rendering of the contact the form page
and processing of form submissions.
It renders the contact form page and handles the submissions.
"""

from django.shortcuts import render
from .forms import ContactForm


def contact_view(request):
    submitted = False
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            submitted = True

    else:
        # If it's a GET request, initialize an empty form
        form = ContactForm()

    # If the form is not valid or it's a GET request, render the contact form
    # page
    return render(
        request,
        "contact/contact_form.html",
        {"form": form, "submitted": submitted},
    )


def contact_success_view(request):
    return render(request, "cakes/index")
