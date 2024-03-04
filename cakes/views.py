from django.shortcuts import render, get_object_or_404
from .models import IndividualCake, CakeCategory


def cake_list(request):
    """
    This view renders a list of cakes that's filtered by the individual
    categories of:
    Wedding, Novelty, and Birthday.

    It does this by querying the database for cake under the categories and
    then passes them to the index.html for rendering under the different
    heading.
    """

    # Fetching the cake categories.
    wedding_category = get_object_or_404(CakeCategory, category="Wedding")
    novelty_category = get_object_or_404(CakeCategory, category="Novelty")
    birthday_category = get_object_or_404(CakeCategory, category="Birthday")
    # Filtering the cakes according to the categories and using prefetch to
    # limit the number of database queries
    wedding_cakes = IndividualCake.objects.filter(
        category=wedding_category
    ).prefetch_related("images")
    novelty_cakes = IndividualCake.objects.filter(
        category=novelty_category
    ).prefetch_related("images")
    birthday_cakes = IndividualCake.objects.filter(
        category=birthday_category
    ).prefetch_related("images")

    # Rendering the cake lists to index.html
    return render(
        request,
        "cakes/index.html",
        {
            "wedding_cakes": wedding_cakes,
            "novelty_cakes": novelty_cakes,
            "birthday_cakes": birthday_cakes,
        },
    )


def cake_detail(request, cake_id):
    """
    Renders the detail page for a cake.
    It retrieves an IndividualCake object by its ID or returns a 404 error
    if it doesn't exist. The cake's details are then passed to the
    'cakes/cake_detail.html' template for display.
    """

    # Getting the cake or gives a 404 error.
    cake = get_object_or_404(IndividualCake, id=cake_id)

    # Renders the individual cake to the cake_detail.html
    return render(request, "cakes/cake_detail.html", {"cake": cake})
