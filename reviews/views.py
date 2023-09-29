"""Module to handle the views that are related to the Post model"""

# render to return a template/page, get_object_or_404 to return a 404
# response if an object isn't found. And redirect to take a user somewhere
# after they have completed a task.  Example being, the home page after
# signing in.
from django.shortcuts import render, get_object_or_404, reverse, redirect

# Provides generic views and view classes for HTTP requests.
from django.views import generic, View

# Module to handle HTTP responses, providing a way to redirect the user to
# a different URL.
from django.http import HttpResponseRedirect

# Importing the post model.
from .models import Post

# Importing the user post Form.
from .forms import UserPostForm


# Much in this file is from the walkthrough project with Hello Django
# Had to change names defining singular and plural to make more sense, both
# here and in other places throughout files.
# Also, have changed "review" to "post" for consistency and to fit with how
# django handles things.


class PostList(generic.ListView):
    """
    Class that represents the a list of the posts.  It defines what is
    displayed and the order it's displayed in.
    """

    # Post is the model that is being used.
    model = Post

    # Order being the most recent.
    queryset = Post.objects.filter(status=1).order_by("-created_on")

    # Name of the template that's used to render the list of posts.
    template_name = "reviews/post_list.html"

    # Limit posts to 6 per page in order for django to automatically add
    # page navigation.
    paginate_by = 6


class PostDetail(View):
    """Class that represents the detail of an individual post."""

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


class PostLike(View):
    """Class that handles the post likes"""

    def post(self, request, slug, *args, **kwargs):
        """
        Toggles the likes.
        """
        # Attempts to get a post with a matching slug field.  If it can't
        # find on then it returns a 404, page not found error.
        post = get_object_or_404(Post, slug=slug)

        # Checks if the current user has already liked the post.
        if post.likes.filter(id=request.user.id).exists():
            # If the user's already liked the post, clicking on it again will unlike it.
            post.likes.remove(request.user)
        else:
            # If the user's not liked it yet, then it's liked when the user clicks on it.
            post.likes.add(request.user)

        # Takes the user back to the post_detail.html
        return HttpResponseRedirect(reverse("post_detail", args=[slug]))


def create_post(request):
    """
    Handles the creation of new posts from the user by checking if the request
    is a POST request.
    if it's not, then it's a GET request and the ELSE statement takes over
    and produces an empty form for the user to use for submitting a post.
    """
    # Checks if request is using the POST method.
    if request.method == "POST":
        # defines the form as holding the users writing and any image
        # files they may have attached.
        form = UserPostForm(request.POST, request.FILES)

        # If the form's valid according to the "UserPostForm" class that
        # inherits the criteria from ModelForm
        if form.is_valid():
            # It's then saved
            new_post = form.save(commit=False)

            # Sets the user's post to draft before it's saved, to ensure
            # it's not posted until it's approved by the admin.
            new_post.status = 0

            #  Saves the post.
            new_post.save()

            # Once the user's post is saved, they're taken back
            # to post_list.html
            return redirect("post_list")
    else:
        # Otherwise a blank form it produced for ether user.
        form = UserPostForm()
    return render(request, "reviews/post_form.html", {"form": form})
