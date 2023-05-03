from rest_framework import serializers
from products.models import Product
from users.models import User


class SellerSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "first_name",
            "last_name",
        ]


class productSerializer(serializers.ModelSerializer):
    seller_id = SellerSerializer()

    class Meta:
        model = Product
        fields = "__all__"
        read_only_fields = [
            "is_avaliable",
            "seller_id",
        ]

    def create(self, validated_data):
        return Product.objects.create(**validated_data)
