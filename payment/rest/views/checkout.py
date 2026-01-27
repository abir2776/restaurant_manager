import decimal

import stripe
from django.conf import settings
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from order.models import CartItem
from order.utils import create_order_from_cart
from payment.models import Payment

stripe.api_key = settings.STRIPE_SECRET_KEY


class CheckoutAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        address_id = request.data.get("address_id")
        payment_type = request.data.get("payment_type")
        errors = {}

        if not address_id:
            errors["address_id"] = "address_id is required"

        if not payment_type:
            errors["payment_type"] = "payment_type is required"

        if errors:
            return Response(errors, status=400)

        cart_items = CartItem.objects.filter(user=request.user)

        if not cart_items.exists():
            return Response({"detail": "Cart is empty"}, status=400)

        order = create_order_from_cart(
            cart_items=cart_items,
            user=request.user,
            address_id=address_id,
            payment_type=payment_type,
        )

        session = stripe.checkout.Session.create(
            mode="payment",
            customer_email=request.user.email,
            metadata={
                "order_id": order.id,
                "payment_type": payment_type,
            },
            line_items=[
                {
                    "price_data": {
                        "currency": "usd",
                        "product_data": {"name": item.product.title},
                        "unit_amount": int(item.product.price * decimal.Decimal(100)),
                    },
                    "quantity": item.quantity,
                }
                for item in cart_items
            ],
            success_url=settings.STRIPE_SUCCESS_URL,
            cancel_url=settings.STRIPE_CANCEL_URL,
        )

        Payment.objects.create(
            user=request.user,
            order=order,
            stripe_session_id=session.id,
            amount=order.total_amount,
            currency="usd",
        )

        return Response({"checkout_url": session.url})
