from django.urls import path

from core.rest.views.token import AdminTokenObtainPairView

urlpatterns = [
    path(
        "",
        AdminTokenObtainPairView.as_view(),
        name="admin_token_obtain_pair",
    ),
]
