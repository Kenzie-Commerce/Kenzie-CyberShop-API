from rest_framework import serializers
from orders.models import Order
from products.models import Product


class ProductsOrdersSerializer(serializers.ModelSerializer):
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


class OrderSerializer(serializers.ModelSerializer):
    product = ProductsOrdersSerializer(read_only=True)

    class Meta:
        model = Order
        fields = "__all__"
        read_only_fields = ["id", "created_at", "user", "seller"]

    def create(self, validated_data: list[dict]) -> Order:
        list_product = validated_data.get("product")
        list_created = []

        for prod in list_product:
            product = Product.objects.get(id=prod["id"])
            list_created.append(
                Order.objects.create(
                    product=product,
                    user=validated_data["user"],
                    seller=product.seller_id,
                )
            )

        return list_created

    def to_representation(self, instance):
        method = self.context["request"].method

        if method == "POST":
            representation = []

            for i in instance:
                representation.append(super().to_representation(i))

            return {"Orders": representation}

        return super().to_representation(instance)
