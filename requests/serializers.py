from rest_framework import serializers
from requests.models import Request
from products.serializers import ProductSerializer
from products.models import Product
import ipdb


class ProductsRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["id", "name", "value", "category", "description", "seller_id"]


class RequestSerializer(serializers.ModelSerializer):
    product = ProductsRequestSerializer(many=True)

    class Meta:
        model = Request
        fields = "__all__"
        read_only_fields = ["id", "product", "created_at", "user", "seller"]
        depth = 1

    def create(self, validated_data: list[dict]) -> Request:
        list_product = validated_data.get("product")
        list_created = []

        for prod in list_product:
            # seller_prod = prod.get("seller_id")
            product = Product.objects.get(id=prod["id"])

            list_created.append(
                Request.objects.create(
                    product=product,
                    user=validated_data["user"],
                    seller=product.seller_id,
                ),
            )

        # ipdb.set_trace()

        return list_created
