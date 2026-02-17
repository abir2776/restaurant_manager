import decimal

import stripe
from django.conf import settings
from rest_framework import serializers
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from core.models import GuestUser
from order.models import CartItem
from order.utils import create_order_from_cart
from payment.models import Payment

stripe.api_key = settings.STRIPE_SECRET_KEY


class CheckoutAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        address_id = request.data.get("address_id")
        payment_type = request.data.get("payment_type")
        cart_item_ids = request.data.get("cart_item_ids", None)
        errors = {}

        if not address_id:
            errors["address_id"] = "address_id is required"

        if not payment_type:
            errors["payment_type"] = "payment_type is required"

        if errors:
            return Response(errors, status=400)

        if cart_item_ids:
            cart_items = CartItem.objects.filter(id__in=cart_item_ids)

        else:
            cart_items = CartItem.objects.filter(user=request.user)
            cart_item_ids = list(cart_items.values_list("id", flat=True))

        if not cart_items.exists():
            return Response({"detail": "Cart is empty"}, status=400)

        if request.user.is_authenticated:
            user = request.user
            email = request.user.email
        else:
            user = None

        if user is None:
            first_name = request.data.get("first_name", None)
            last_name = request.data.get("last_name", None)
            email = request.data.get("email", None)
            phone = request.data.get("phone", None)
            if (
                first_name is None
                or last_name is None
                or email is None
                or phone is None
            ):
                raise serializers.ValidationError("User information is not provided!")
            guest_user = GuestUser.objects.create(
                first_name=first_name, last_name=last_name, email=email, phone=phone
            )

        order = create_order_from_cart(
            cart_items=cart_items,
            user=user,
            guest_user=guest_user,
            address_id=address_id,
            payment_type=payment_type,
        )

        session = stripe.checkout.Session.create(
            mode="payment",
            customer_email=email,
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
            user=user,
            guest_user=guest_user,
            order=order,
            stripe_session_id=session.id,
            amount=order.total_amount,
            cart_ids=cart_item_ids,
            currency="usd",
        )

        return Response({"checkout_url": session.url})
