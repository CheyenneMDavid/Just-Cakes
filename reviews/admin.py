from django.contrib import admin
from .models import Reviews
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Reviews)
class ReviewsAdmin(SummernoteModelAdmin):
    """
    Use to define how the Admin manages reviews
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
