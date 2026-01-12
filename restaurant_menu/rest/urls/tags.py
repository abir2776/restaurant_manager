from django.urls import path

from restaurant_menu.rest.views.tags import TagDetailsAPIView, TagListCreateAPIView

urlpatterns = [
    path("", TagListCreateAPIView.as_view(), name="tag-list"),
    path("/<int:id>", TagDetailsAPIView.as_view(), name="tag-details"),
]
