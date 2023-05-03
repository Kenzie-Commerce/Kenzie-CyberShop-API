from rest_framework import serializers
from products.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"
        read_only_fields = [
            "is_avaliable",
            "seller_id",
        ]

    def create(self, validated_data: dict):
        return Product.objects.create(**validated_data)

    def update(self, instance: Product, validated_data: dict):
        if validated_data["stock"] > 0:
            instance.is_avaliable = True
        else:
            instance.is_avaliable = False
        return super().update(instance, validated_data)
