# urls.py

from django.urls import path

from order.rest.views.cart import (
    CartItemListCreateView,
    CartItemRetrieveUpdateDestroyView,
)

urlpatterns = [
    path("", CartItemListCreateView.as_view(), name="cart-list-create"),
    path(
        "<int:pk>", CartItemRetrieveUpdateDestroyView.as_view(), name="cart-detail"
    ),
]
