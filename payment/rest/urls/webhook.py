from django.urls import path

from payment.rest.views.webhook import stripe_webhook

urlpatterns = [path("", stripe_webhook)]
