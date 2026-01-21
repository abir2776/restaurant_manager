from django.urls import path

from payment.rest.views.checkout import CheckoutAPIView

urlpatterns = [path("", CheckoutAPIView.as_view())]
