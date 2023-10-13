# Import required modules
from django import forms
from .models import Post


class UserPostForm(forms.ModelForm):
    """Form for creating and editing user posts, by the user."""

    class Meta:
        model = Post
        # The fields that are used by the forms a user fills in when
        # submitting a post.
        fields = (
            "title",
            "content",
            "featured_image",
        )
