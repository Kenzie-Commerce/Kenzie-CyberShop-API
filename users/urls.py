from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView


urlpatterns = [
    path("users/"),
    path("users/<int:id_user>/"),
    path("users/login/", TokenObtainPairView.as_view()),
    path("users/login/refresh/", TokenObtainPairView.as_view()),
]
