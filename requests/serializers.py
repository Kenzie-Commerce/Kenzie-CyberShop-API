from rest_framework import serializers
from requests.models import Request
from products.models import Product
import ipdb


class ProductsRequestSerializer(serializers.ModelSerializer):
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


class RequestSerializer(serializers.ModelSerializer):
    product = ProductsRequestSerializer(read_only=True)

    class Meta:
        model = Request
        fields = "__all__"
        read_only_fields = ["id", "created_at", "user", "seller"]

    def create(self, validated_data: list[dict]) -> Request:
        list_product = validated_data.get("product")
        list_created = []

        for prod in list_product:
            product = Product.objects.get(id=prod["id"])
            list_created.append(
                Request.objects.create(
                    product=product,
                    user=validated_data["user"],
                    seller=product.seller_id,
                )
            )

        return list_created

    def to_representation(self, instance):
        representation = []
        for i in instance:
            representation.append(super().to_representation(i))
        return {"Request": representation}
