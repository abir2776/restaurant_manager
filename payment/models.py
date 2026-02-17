from django.contrib.postgres.fields import ArrayField
from django.db import models

from core.models import GuestUser, User
from order.models import Order


class Payment(models.Model):
    STATUS_CHOICES = (
        ("PENDING", "Pending"),
        ("SUCCESS", "Success"),
        ("FAILED", "Failed"),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    guest_user = models.ForeignKey(
        GuestUser, on_delete=models.CASCADE, null=True, blank=True
    )
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    stripe_session_id = models.CharField(max_length=255, unique=True)
    amount = models.IntegerField()
    currency = models.CharField(max_length=10)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="PENDING")
    created_at = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    cart_ids = ArrayField(models.IntegerField(max_length=255), blank=True, default=list)
