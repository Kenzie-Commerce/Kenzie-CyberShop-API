from rest_framework import serializers
from addresses.models import Address


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = [
            "id",
            "street",
            "number",
            "complement",
            "district",
            "default",
            "user",
        ]
        read_only_fields = ["complement", "user"]

    def create(self, validated_data: dict) -> Address:
        user = validated_data["user"]

        if not user.addresses.count():
            return Address.objects.create(**validated_data, default=True)
        else:
            return Address.objects.create(**validated_data)

    def update(self, instance, validated_data):
        user = validated_data["user"]

        if validated_data.get("default"):
            address = Address.objects.get(user=user.id, default=True)
            address.default = False
            address.save()

        return super().update(instance, validated_data)
