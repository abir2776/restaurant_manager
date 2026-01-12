# urls.py

from django.urls import path

from order.rest.views.order import OrderListCreateView, OrderRetrieveUpdateDestroyView

urlpatterns = [
    path("", OrderListCreateView.as_view(), name="order-list-create"),
    path("<int:pk>/", OrderRetrieveUpdateDestroyView.as_view(), name="order-detail"),
]
