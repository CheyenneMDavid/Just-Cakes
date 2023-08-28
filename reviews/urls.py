# Importing the required modules
from . import views
from django.urls import path


# URL patterns for the reviews application.
urlpatterns = [
    path("", views.ReviewsList.as_view(), name="reviews_list"),
    path("<slug:slug>/", views.ReviewsDetail.as_view(), name="reviews_detail"),
]
