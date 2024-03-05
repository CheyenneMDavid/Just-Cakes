"""
Purpose of this view is to handle the rendering of the contact the form page
and processing of form submissions.
It renders the contact form page and handles the submissions.
"""

from django.shortcuts import render
from .forms import ContactForm


def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ContactForm()
    return render(request, "contact/contact_form.html", {"form": form})
