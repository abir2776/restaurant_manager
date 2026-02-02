from django.urls import path

from restaurant_menu.rest.views.opening_hours import (
    OpeningHoursDetailsAPIView,
    OpeningHoursListCreateAPIView,
)

urlpatterns = [
    path("", OpeningHoursListCreateAPIView.as_view(), name="opening-hours-list-create"),
    path(
        "<int:id>", OpeningHoursDetailsAPIView.as_view(), name="opening-hours-details"
    ),
]
