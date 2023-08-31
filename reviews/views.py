# Imports the required modules and models.
from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Post


# Much in this file is from the walkthrough project with Hello Django
# Had to change names defining singular and plural to make more sense, both
# here and in other places throughout files.
# Also, have changed "review" to "post" for consistency and to fit with how
# django handles things.


class PostList(generic.ListView):
    model = Post
    # Defines what is displayed and the order in which it is displayed.
    # Order being the most recent.
    queryset = Post.objects.filter(status=1).order_by("-created_on")

    # Name of the template that's used to render the list of posts.
    template_name = "reviews/post_list.html"

    # Limit posts to 6 per page in order for django to automatically add
    # page navigation.
    paginate_by = 6


# Handles the detail view of a post.
class PostDetail(View):
    def get(self, request, slug, *args, **kwargs):
        """Handles the get request for the detail view of a post"""

        # Returns published posts.
        queryset = Post.objects.filter(status=1)

        # Tries to return a post or raises a 404 error if not found.
        post = get_object_or_404(queryset, slug=slug)

        # Used as a toggle for liking and unliking. Having it as false, which
        # is the default is essentially keeping it at unliked until liked.
        liked = False

        # Checks if the user likes the post.
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        # Renders the detail view.
        return render(
            request,
            "reviews/post_detail.html",
            {"post": post, "liked": liked},
        )


# Handles the post likes.
class PostLike(View):
    def post(self, request, slug, *args, **kwargs):
        """
        Toggles the like and unlikes
        """
        post = get_object_or_404(Post, slug=slug)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse("post_detail", args=[slug]))
