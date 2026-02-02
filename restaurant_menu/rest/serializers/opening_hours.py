from rest_framework import serializers

from restaurant_menu.models import OpeningHours


class OpeningHoursSerializer(serializers.ModelSerializer):
    class Meta:
        model = OpeningHours
        fields = "__all__"
