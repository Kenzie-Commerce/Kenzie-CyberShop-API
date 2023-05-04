from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView
from addresses.views import AddressView, AddressDetailView


urlpatterns = [
    # path("users/"),
    # path("users/<int:id_user>/"),
    path("users/login/", TokenObtainPairView.as_view()),
    path("users/login/refresh/", TokenObtainPairView.as_view()),
    path("users/address/", AddressView.as_view()),
    path("users/address/<str:address_id>/", AddressDetailView.as_view()),
]
