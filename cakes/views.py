# Import all required modules
from django.shortcuts import render, get_object_or_404
from .models import IndividualCake


# To view the cake list.
def cake_list(request):
    """Renders a list of all the cakes"""

    # Using "prefetch_related('images').all()" to tell Django to fetch all
    # related images for the IndividualCake in just one database query which
    # reduces the amount of queries made.  Currently there is only one image
    # per IndividualCake, but when this changes, using the prefetch_related
    # will be be more efficient.
    cakes = IndividualCake.objects.prefetch_related("images").all()

    # Returns the cake_list.html
    return render(request, "cakes/cakes_list.html", {"cakes": cakes})


# To view the cake details
def cake_detail(request, cake_id):
    """Render the view of an individual cake"""

    # Returns individual cake or returns a 404 error if the cake's not found.
    cake = get_object_or_404(IndividualCake, id=cake_id)

    return render(request, "cakes/cakes_detail.html", {"cake": cake})


# To view the categorized cake list.
def categorized_cake_list(request):
    """
    lists cakes filtered by their category, in order to enable the list of
    cakes to be displayed by category on the landing page.
    """
    # Query for cakes with the 'wedding' category.
    wedding_cakes = IndividualCake.objects.filter(category="wedding")
    # Query for cakes with the 'birthday' category.
    birthday_cakes = IndividualCake.objects.filter(category="birthday")
    # Query for cakes with the 'novelty' category.
    novelty_cakes = IndividualCake.objects.filter(category="novelty")

    # Returns a html with the listed cake categories.
    return render(
        request,
        "cakes/categorized_cake_list.html",
        {
            "wedding_cakes": wedding_cakes,
            "birthday_cakes": birthday_cakes,
            "novelty_cakes": novelty_cakes,
        },
    )
