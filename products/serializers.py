from rest_framework import serializers
from products.models import Product


class productSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"
        read_only_fields = [
            "is_avaliable",
            "seller_id",
        ]

    def create(self, validated_data):
        return Product.objects.create(**validated_data)
