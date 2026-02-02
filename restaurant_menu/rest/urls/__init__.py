from django.urls import include, path

urlpatterns = [
    path("category/", include("restaurant_menu.rest.urls.category")),
    path("images/", include("restaurant_menu.rest.urls.images")),
    path("tags/", include("restaurant_menu.rest.urls.tags")),
    path("products/", include("restaurant_menu.rest.urls.products")),
    path("opening-hours/", include("restaurant_menu.rest.urls.opening_hours")),
]
