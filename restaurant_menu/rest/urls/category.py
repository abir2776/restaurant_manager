from django.urls import path

from restaurant_menu.rest.views.category import (
    CategoryDetailAPIView,
    CategoryListCreateAPIView,
    FoodCategoryDetailAPIView,
    FoodCategoryListCreateAPIView,
)

urlpatterns = [
    path("", CategoryListCreateAPIView.as_view(), name="category-list"),
    path("<int:id>", CategoryDetailAPIView.as_view(), name="category-details"),
    path("food", FoodCategoryListCreateAPIView.as_view(), name="food-category-list"),
    path(
        "/food/<int:id>",
        FoodCategoryDetailAPIView.as_view(),
        name="food-category-detail",
    ),
]
