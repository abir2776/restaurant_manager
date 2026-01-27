from django.urls import include, path

urlpatterns = [
    path("users/", include("core.rest.urls.users")),
    path("orders/", include("core.rest.urls.orders")),
    path("transactions/", include("core.rest.urls.transactions")),
]
