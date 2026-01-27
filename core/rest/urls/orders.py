from django.urls import path

from core.rest.views.orders import AdminOrderDetailsView, AdminOrderListView

urlpatterns = [
    path("", AdminOrderListView.as_view(), name="admin-order-list"),
    path("<int:pk>", AdminOrderDetailsView.as_view(), name="admin-order-details"),
]
