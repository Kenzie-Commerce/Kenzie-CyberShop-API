from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView
from addresses.views import AddressView, AddressDetailView
from carts.views import CartListView
from requests.views import RequestViews, RequestDetailViews

urlpatterns = [
    # path("users/"),
    # path("users/<int:id_user>/"),
    path("users/login/", TokenObtainPairView.as_view()),
    path("users/login/refresh/", TokenObtainPairView.as_view()),
    path("users/address/", AddressView.as_view()),
    path("users/address/<str:address_id>/", AddressDetailView.as_view()),
    path("users/cart/", CartListView.as_view()),
    path("users/requests/", RequestViews.as_view()),
    path("users/requests/<str:request_id>/", RequestDetailViews.as_view()),
]
