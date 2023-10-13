"""Importing required modules for URL configuration and views"""
import os
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.static import serve
from django.conf import settings

# Much in this file is from the walkthrough project with Hello Django
# Had to change names defining singular and plural to make more sense, both
# here and in other places throughout files.
# Also, have changed "review" to "post" for consistency and to fit with how
# django handles things.

# URL patterns for overall project.
urlpatterns = [
    path("admin/", admin.site.urls),
    path("customer_accounts/", include("customer_accounts.urls")),
    path("summernote/", include("django_summernote.urls")),
    path("", include("cakes.urls")),
    path("reviews/", include("reviews.urls")),
    path("account/", include("allauth.urls")),
    # url pattern to load the favicon.ico from the static folder.
    re_path(
        r"^favicon.ico$",
        serve,
        {
            "document_root": os.path.join(settings.BASE_DIR, "local_static"),
            "path": "favicon.ico",
        },
    ),
]
