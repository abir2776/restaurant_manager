from django.urls import path

from restaurant_menu.rest.views.dashboard import OrderStatsAPIView, ProductStatsAPIView

urlpatterns = [
    path("orders", OrderStatsAPIView.as_view(), name="orders-count"),
    path("products", ProductStatsAPIView.as_view(), name="products-count"),
]
