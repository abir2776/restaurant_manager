# payments/webhooks.py
import stripe
from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from order.models import CartItem
from payment.models import Payment

stripe.api_key = settings.STRIPE_SECRET_KEY


@csrf_exempt
def stripe_webhook(request):
    payload = request.body
    sig_header = request.META.get("HTTP_STRIPE_SIGNATURE")

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, settings.STRIPE_WEBHOOK_SECRET
        )
    except Exception:
        return HttpResponse(status=400)

    if event["type"] == "checkout.session.completed":
        session = event["data"]["object"]
        payment = Payment.objects.get(stripe_session_id=session["id"])
        payment.status = "SUCCESS"
        CartItem.objects.filter(id__in=payment.cart_ids).delete()

    if event["type"] == "payment_intent.payment_failed":
        intent = event["data"]["object"]
        Payment.objects.filter(stripe_session_id=intent["id"]).update(status="FAILED")

    return HttpResponse(status=200)
