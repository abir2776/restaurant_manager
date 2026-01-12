from django.urls import path

from restaurant_menu.rest.views.images import ImageDetailsView, ImageListCreateView

urlpatterns = [
    path("", ImageListCreateView.as_view(), name="image-list-create"),
    path("<int:id>", ImageDetailsView.as_view(), name="image-details"),
]
