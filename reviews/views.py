# Imports the required modules.
from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Reviews


class ReviewsList(generic.ListView):
    model = Reviews
    # Defines whast is displayed and the order in which it is displayed.
    # Order being the most recent.
    queryset = Reviews.objects.filter(status=1).order_by("-created_on")

    # Name of the template that's used to render the list of reviews.
    template_name = "reviews_list.html"

    # Limit reviews to 6 per page in order for django to automatically add
    # page navigation.
    paginate_by = 6


class ReviewsDetail(View):
    def get(self, request, slug, *args, **kwargs):
        """Handles the get request"""

        # Returns published reviews
        queryset = Reviews.objects.filter(status=1)

        # Tries to return a review or raises a 404 error.
        reviews = get_object_or_404(queryset, slug=slug)

        # Used as a toggle for liking and unliking. Having it as false, which
        # is the default is essentially keeping it at unliked until liked.
        liked = False

        # Checks if the user likes the review.
        if reviews.likes.filter(id=self.request.user.id).exists():
            liked = True

        # Returns page.
        return render(
            request,
            "reviews/reviews_detail.html",
            {"reviews": reviews, "liked": liked},
        )
