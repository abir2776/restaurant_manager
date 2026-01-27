from django.urls import include, path

urlpatterns = [path("users/", include("core.rest.urls.users"))]
