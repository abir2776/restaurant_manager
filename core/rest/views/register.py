from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from ..serializers import register


class PublicUserRegistration(APIView):
    authentication_classes = []
    permission_classes = [AllowAny]

    def post(self, request, format=None):
        serializer = register.PublicUserRegistrationSerializer(
            data=request.data, context={"request": request}
        )

        if serializer.is_valid():
            user = serializer.save()
            email = request.data.get("email")
            password = request.data.get("password")
            user = authenticate(request, email=email, password=password)

            if not user:
                return Response(
                    {"detail": "Authentication failed after registration"},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            refresh = RefreshToken.for_user(user)

            return Response(
                {
                    "access": str(refresh.access_token),
                    "refresh": str(refresh),
                    "user": {
                        "id": user.id,
                        "email": user.email,
                    },
                },
                status=status.HTTP_201_CREATED,
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
