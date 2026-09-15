from django.urls import path

from . import views  # "." means the current package; import the sibling views.py module.

urlpatterns = [
    path("", views.index, name="index"),
    path("product/<int:product_id>", views.product_detail, name="product_detail"),
    path("accounts/login/", views.login_view, name="login_view"),
]
