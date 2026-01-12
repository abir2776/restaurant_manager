from django.urls import path

from restaurant_menu.rest.views.products import (
    ProductDetailsAPIView,
    ProductListCreateAPIView,
)

urlpatterns = [
    path("", ProductListCreateAPIView.as_view(), name="product-list-create"),
    path("<int:id>", ProductDetailsAPIView.as_view(), name="product-details"),
]
