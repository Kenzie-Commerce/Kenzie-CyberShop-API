from rest_framework import serializers
from carts.models import Cart
from products.models import Product
from users.models import User


class CartProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            "id",
            "name",
            "value",
            "category",
            "description",
            "seller_id",
        ]


class CartUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "email",
        ]


class CartSerializer(serializers.ModelSerializer):
    products = CartProductSerializer(read_only=True, many=True)
    user = CartUserSerializer(read_only=True)

    class Meta:
        model = Cart
        fields = "__all__"

    def create(self, validated_data):
        user = validated_data["user"]
        product = validated_data.pop("products")

        if not user.carts.count():
            cart = Cart.objects.create(**validated_data)
            cart.products.set([product])
            cart.save()
            return cart

        cart = Cart.objects.get(user=user)
        cart.products.add(product)
        cart.save()

        return cart
