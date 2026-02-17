from .models import Order, OrderItem


def create_order_from_cart(cart_items, user, guest_user, address_id, payment_type):
    order = Order.objects.create(
        user=user,
        guest_user=guest_user,
        address_id=address_id,
        payment_type=payment_type,
        total_amount=0,
    )

    total = 0
    for item in cart_items:
        OrderItem.objects.create(
            order=order,
            product=item.product,
            quantity=item.quantity,
            price=item.total_price,
        )
        total += item.total_price

    order.total_amount = total
    order.save()

    return order
