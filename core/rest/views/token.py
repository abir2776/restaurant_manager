from rest_framework_simplejwt.views import TokenObtainPairView

from core.rest.serializers.token import AdminTokenObtainPairSerializer


class AdminTokenObtainPairView(TokenObtainPairView):
    serializer_class = AdminTokenObtainPairSerializer
