from django.urls import path

from core.rest.views.users import (
    AdminUserDetailsView,
    AdminUserListView,
    AdminUserOrderListView,
)

urlpatterns = [
    path("", AdminUserListView.as_view(), name="admin-user-list"),
    path("<int:pk>", AdminUserDetailsView.as_view(), name="admin-user-details"),
    path(
        "<int:user_id>/orders", AdminUserOrderListView.as_view(), name="admin-user-list"
    ),
    path("orders/<int:pk>", AdminUserDetailsView.as_view(), name="admin-user-details"),
]
