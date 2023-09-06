# Import all required modules
from django.shortcuts import render, get_object_or_404
from .models import Cake


# To view the cake list.
def cake_list(request):
    """Renders a list of all the cakes"""

    # Fetches all the cake objects to display in the cake_list.html
    cakes = Cake.objects.all()
    # Returns the cake_list.html
    return render(request, "cakes/cakes_list.html", {"cakes": cakes})


# To view the cake details
def cake_detail(request, cake_id):
    """Render the view of an indiviual cake"""

    # Returns individual cake or returns a 404 error if the cake's not found.
    cake = get_object_or_404(Cake, id=cake_id)
    return render(request, "cakes/cake_detail.html", {"cake": cake})
