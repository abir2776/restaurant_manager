from django.urls import include, path

urlpatterns = [
    path("checkout/", include("payment.rest.urls.checkout")),
    path("webhook/", include("payment.rest.urls.webhook")),
]
