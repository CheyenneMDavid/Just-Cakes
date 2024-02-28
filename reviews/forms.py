# Import required modules
from django import forms
from .models import Post, Comment


class UserPostForm(forms.ModelForm):
    """Form for creating and editing user posts"""

    class Meta:
        model = Post
        # The fields that are used by the forms a user fills in when
        # submitting a post.
        fields = (
            "title",
            "content",
            "featured_image",
        )


class CommentForm(forms.ModelForm):
    """
    Form for creating comments on posts.
    """

    class Meta:
        model = Comment
        fields = ("body",)
