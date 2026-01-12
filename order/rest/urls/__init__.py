from django.urls import include, path

urlpatterns = [
    path("cart/", include("order.rest.urls.cart")),
    path("", include("order.rest.urls.order")),
]
