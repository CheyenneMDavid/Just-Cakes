# Importing the required modules
from django.urls import path
from . import views


# Much in this file is from the walkthrough project with Hello Django
# Had to change names defining singular and plural to make more sense, both
# here and in other places throughout files.
# Also, have changed "review" to "post" for consistency and to fit with how
# django handles things.

# URL patterns for the reviews application.
urlpatterns = [
    path("", views.PostList.as_view(), name="post_list"),
    # path("create-post/", views.CreatePostView.as_view(), name="create_post"),
    path("<slug:slug>/", views.PostDetail.as_view(), name="post_detail"),
    path("like/<slug:slug>", views.PostLike.as_view(), name="post_like"),
]
