from datetime import timedelta

from django.db.models import Count, Q
from django.utils.timezone import now
from rest_framework.response import Response
from rest_framework.views import APIView

from order.models import Order
from restaurant_menu.models import Product


class OrderStatsAPIView(APIView):
    def get(self, request):
        days = request.query_params.get("days")  # 3,7,10,15,30

        queryset = Order.objects.all()

        if days:
            try:
                days = int(days)
                start_date = now() - timedelta(days=days)
                queryset = queryset.filter(created_at__gte=start_date)
            except ValueError:
                return Response(
                    {"success": False, "message": "Invalid days parameter"},
                    status=400,
                )

        data = queryset.aggregate(
            pending=Count("id", filter=Q(status="pending")),
            processing=Count("id", filter=Q(status="processing")),
            shipped=Count("id", filter=Q(status="shipped")),
            delivered=Count("id", filter=Q(status="delivered")),
            cancelled=Count("id", filter=Q(status="cancelled")),
            total=Count("id"),
        )

        return Response({"success": True, "filters": {"last_days": days}, "data": data})


class ProductStatsAPIView(APIView):
    def get(self, request):
        days = request.query_params.get("days")  # 3,7,10,15,30

        queryset = Product.objects.all()

        if days:
            try:
                days = int(days)
                start_date = now() - timedelta(days=days)
                queryset = queryset.filter(created_at__gte=start_date)
            except ValueError:
                return Response(
                    {"success": False, "message": "Invalid days parameter"},
                    status=400,
                )

        total_products = queryset.count()

        return Response(
            {
                "success": True,
                "filters": {"last_days": days},
                "data": {"total_products": total_products},
            }
        )
