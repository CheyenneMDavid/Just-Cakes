"""
Module to handle the views that are related to the Post model
 Much in this file is from the walkthrough project with Hello Django
Had to change names defining singular and plural to make more sense, both
here and in other places throughout files.
Also, have changed "review" to "post" for consistency and to fit with how
django handles things.
"""

# render to return a template/page, get_object_or_404 to return a 404
# response if an object isn't found. And redirect to take a user somewhere
# after they have completed a task.  Example being, the home page after
# signing in.
from django.shortcuts import render, get_object_or_404, reverse
from django.views.generic.edit import CreateView, DeleteView
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Post
from .forms import CommentForm, UserPostForm
from django.urls import reverse_lazy
from django.contrib import messages


class PostList(generic.ListView):
    """
    Class that represents the a list of the posts.  It defines what is
    displayed and the order it's displayed in.
    """

    model = Post
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "reviews/post_list.html"
    paginate_by = 6


class PostDetail(View):
    """Class that represents the detail of an individual post."""

    def get(self, request, slug, *args, **kwargs):
        """Handles the get request for the detail view of a post"""

        # filtering posts by their status.
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)

        # Retrieving comments for a post.
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        # Rendering the post detail page.
        return render(
            request,
            "reviews/post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm(),
            },
        )

    def post(self, request, slug, *args, **kwargs):
        """
        Handles the post request for the detail view of a post
        """

        # Filtering the posts by their status.
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)

        # Retrieving the comments for a post
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False

        # Checking if a post if liked by the current user.
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        # Processing the comment submission.
        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.name = request.user.username
            new_comment.email = request.user.email
            new_comment.save()
        else:
            comment_form = CommentForm()

        # Rendering the detail page
        return render(
            request,
            "reviews/post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "comment_form": comment_form,
                "liked": liked,
            },
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

        # Toggles the likes
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        #  Redirecting to the post detail page after the likes are toggled.
        return HttpResponseRedirect(reverse("post_detail", args=[slug]))


class CreatePostView(CreateView):
    """
    This view handles the creation of a new post through a form. Upon
    the successful submission, the user is redirects to the post list and
    displays a success message before timing out.
    """

    model = Post
    form_class = UserPostForm
    template_name = "reviews/post_form.html"
    success_url = reverse_lazy(
        "post_list"
    )  # Redirect to this URL after successful form submission

    def form_valid(self, form):
        """
        Calling the form_valid method upon form submission and a success
        message upon redirection.
        """
        response = super().form_valid(
            form
        )  # This calls the save and redirects to success_url
        messages.success(
            self.request,
            "Thank you for your post submission. As soon as it is approved, "
            "it will be displayed.",
        )
        return response


class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy("post_list")

    def get_success_url(self):
        """
        This view handles thr deletion of a post, and then uses the
        success_url to return the user to the index page which is the list of
        posts.
        """
        return self.success_url
