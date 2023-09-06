# Import required modules
from django.urls import path
from . import views

# List of the url patterns in the app.
urlpatterns = [
    path("", views.cake_list, name="cake_list"),
    # Uses an integer as part of the url because of the way the cake is listed.
    path("<int:cake_id>/", views.cake_detail, name="cake_detail"),
]
