# Import required modules
from django import forms
from .models import Post


class UserPostForm(forms.ModelForm):
    """Form for creating and editing user posts, by the user."""

    class Meta:
        model = Post
        # The fields that are used by the forms a user fils in when
        # submitting a post.
        fields = (
            "title",
            "content",
            # This automatically gets set to zero which keeps it
            # as unpublised until the admin approves it.
            "status",
            "featured_image",
            "excerpt",
        )
