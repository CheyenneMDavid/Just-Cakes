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
from django.views.generic.edit import CreateView
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Post
from .forms import CommentForm, UserPostForm
from django.urls import reverse_lazy


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
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)

        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True
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
        Handles the get request for the detail view of a post
        """
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.name = request.user.username
            new_comment.email = request.user.email
            new_comment.save()
        else:
            comment_form = CommentForm()
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

        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse("post_detail", args=[slug]))


class CreatePostView(CreateView):
    model = Post

    form_class = UserPostForm

    template_name = "reviews/post_form.html"

    success_url = reverse_lazy("post_list")
