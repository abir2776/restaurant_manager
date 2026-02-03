import logging

from rest_framework import serializers

from core.models import User

logger = logging.getLogger(__name__)


class PublicUserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField()

    class Meta:
        model = User
        fields = "__all__"

    def validate_email(self, data):
        email = data.lower()
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError("User with email already exists!")
        return data

    def validate_phone(self, data):
        phone = data
        if User.objects.filter(phone=phone).exists():
            raise serializers.ValidationError("User with phone already exists!")
        return data

    def create(self, validated_data, *args, **kwargs):
        email = validated_data["email"].lower()
        phone = validated_data["phone"]
        first_name = validated_data["first_name"]
        last_name = validated_data["last_name"]
        password = validated_data["password"]

        user = User.objects.create(
            email=email,
            username=email,
            phone=phone,
            first_name=first_name,
            last_name=last_name,
            is_active=True,
        )
        user.set_password(password)
        user.save()
        logger.debug(f"Created new user: {user}")
        return user
