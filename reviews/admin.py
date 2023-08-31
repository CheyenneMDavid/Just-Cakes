# Imports the required modules and models.
from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post

# Much in this file is from the walkthrough project with Hello Django
# Had to change names defining singular and plural to make more sense, both
# here and in other places throughout files.
# Also, have changed "review" to "post" for consistency and to fit with how
# django handles things.


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    """
    Use to define how the Admin manages posts.
    """

    # defines which fields of the model are displayed on the change list
    # page of the admin.
    list_display = ("title", "slug", "status", "created_on")

    # Defines the fields that can be used in the admin search
    search_fields = ["title", "content"]

    # Defines the filter that the admin can filter by.
    list_filter = ("status", "created_on")

    # Automatically generates a slug according to the title.
    prepopulated_fields = {"slug": ("title",)}

    # Defines which of the fields can use the text editor.
    summernote_fields = ("content",)
