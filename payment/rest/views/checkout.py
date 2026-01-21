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
        cart_items = CartItem.objects.filter(user=request.user)

        if not cart_items.exists():
            return Response({"detail": "Cart is empty"}, status=400)

        order = create_order_from_cart(cart_items, request.user)

        session = stripe.checkout.Session.create(
            mode="payment",
            customer_email=request.user.email,
            metadata={"order_id": order.id},
            line_items=[
                {
                    "price_data": {
                        "currency": "usd",
                        "product_data": {"name": item.product.title},
                        "unit_amount": item.product.price,
                    },
                    "quantity": item.quantity,
                }
                for item in cart_items
            ],
            success_url="http://localhost:3000/payment-success",
            cancel_url="http://localhost:3000/cart",
        )

        Payment.objects.create(
            user=request.user,
            order=order,
            stripe_session_id=session.id,
            amount=order.total_amount,
        )

        return Response({"checkout_url": session.url})
