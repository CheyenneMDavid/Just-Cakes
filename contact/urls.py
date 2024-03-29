from django.urls import path
from . import views

# url patterns for contact app which manages contact form submissions
urlpatterns = [
    path("", views.contact_view, name="contact_us"),
    path("success/", views.contact_success_view, name="contact_success"),
]
