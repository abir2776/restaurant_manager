from decimal import Decimal

from django.db.models import Sum
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

from order.models import Order
from restaurant_menu.models import Product


class DashboardAPIView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        total_revenue = Order.objects.filter(status="delivered").aggregate(
            total=Sum("total_amount")
        )["total"] or Decimal("0.00")
        total_orders = Order.objects.count()
        active_menu = Product.objects.filter(status="active").count()

        return Response(
            {
                "total_revenue": total_revenue,
                "total_orders": total_orders,
                "active_menu": active_menu,
            }
        )
