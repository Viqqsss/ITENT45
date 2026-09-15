from django.urls import path

from . import views  # "." means the current package; import the sibling views.py module.

urlpatterns = [
    path("", views.index, name="index"),
]
