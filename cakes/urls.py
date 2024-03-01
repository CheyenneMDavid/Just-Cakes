# Import required modules
from django.urls import path
from . import views

# List of the url patterns in the app.
urlpatterns = [
    path("", views.cake_list, name="index"),
    # URL pattern for individual cake details. The <int:cake_id> captures
    # the cake's ID from the URL and passes it as an argument to the
    # cake_detail view.
    path("<int:cake_id>/", views.cake_detail, name="cake_detail"),
]
