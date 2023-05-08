from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView
from users.views import UserView, UserDetailView
from addresses.views import AddressView, AddressDetailView
from carts.views import CartListView


urlpatterns = [
    path("users/", UserView.as_view()),
    path("users/<int:id_user>/", UserDetailView.as_view()),
    path("users/login/", TokenObtainPairView.as_view()),
    path("users/login/refresh/", TokenObtainPairView.as_view()),
    path("users/address/", AddressView.as_view()),
    path("users/address/<str:address_id>/", AddressDetailView.as_view()),
    path("users/cart/", CartListView.as_view()),
]
