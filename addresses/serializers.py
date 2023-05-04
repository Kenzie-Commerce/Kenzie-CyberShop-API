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
            "user",
        ]
        read_only_fields = ["complement", "user"]

    def create(self, validated_data: dict) -> Address:
        return Address.objects.create(**validated_data)
