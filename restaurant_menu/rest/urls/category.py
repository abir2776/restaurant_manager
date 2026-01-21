from django.urls import path

from restaurant_menu.rest.views.category import (
    CategoryDetailAPIView,
    CategoryListCreateAPIView,
)

urlpatterns = [
    path("", CategoryListCreateAPIView.as_view(), name="category-list"),
    path("<int:id>", CategoryDetailAPIView.as_view(), name="category-details"),
]
