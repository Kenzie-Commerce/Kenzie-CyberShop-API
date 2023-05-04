from carts.models import Cart
from rest_framework import status
from django.http import Http404
from products.models import Product
from carts.serializers import CartSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import (
    RetrieveAPIView,
    get_object_or_404,
    DestroyAPIView,
    CreateAPIView,
)
from rest_framework_simplejwt.authentication import JWTAuthentication


class CartListView(RetrieveAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    pagination_class = None

    queryset = Cart.objects.all()
    serializer_class = CartSerializer

    def get_object(self):
        return get_object_or_404(Cart, user=self.request.user)


class AddOrRemoveProdInCartView(CreateAPIView, DestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    lookup_field = "id_product"
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

    def perform_create(self, serializer: CartSerializer):
        product = get_object_or_404(
            Product,
            id=self.kwargs["id_product"],
        )

        return serializer.save(products=product, user=self.request.user)

    def get_object(self):
        product = get_object_or_404(Product, id=self.kwargs[self.lookup_field])
        return product

    def perform_destroy(self, instance):
        cart = Cart.objects.get(user=self.request.user)

        if instance in cart.products.all():
            list_cart = cart.products.exclude(id=instance.id)
            cart.products.set(list_cart)
            cart.save()
            if not cart.products.count():
                cart.delete()
        else:
            raise Http404
        return Response(status=status.HTTP_204_NO_CONTENT)
