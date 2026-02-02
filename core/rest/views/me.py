from rest_framework.generics import RetrieveUpdateDestroyAPIView

from core.rest.serializers.me import MeSerializer


class MeAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = MeSerializer

    def get_object(self):
        return self.request.user
