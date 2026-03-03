from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class AdminTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)

        allowed_roles = ["ADMIN", "SUPER_ADMIN"]

        if self.user.role not in allowed_roles:
            raise serializers.ValidationError(
                "You are not authorized to access this endpoint."
            )

        return data
