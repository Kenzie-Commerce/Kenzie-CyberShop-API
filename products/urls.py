from django.urls import path
from products.views import ProductView, ProductDetailView


urlpatterns = [
    path("products/", ProductView.as_view()),
    path("products/<str:id_product>/", ProductDetailView.as_view()),
]
