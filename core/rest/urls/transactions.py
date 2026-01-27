from django.urls import path

from core.rest.views.transactions import (
    AdminTransactionDetailsAPIView,
    AdminTransactionListAPIView,
)

urlpatterns = [
    path("", AdminTransactionListAPIView.as_view(), name="admin-transaction-list"),
    path(
        "<int:pk>",
        AdminTransactionDetailsAPIView.as_view(),
        name="admin-transaction-details",
    ),
]
