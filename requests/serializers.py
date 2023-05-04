from rest_framework import serializers
from requests.models import Request


class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request
        fields = "__all__"
        read_only_fields = [
            "id",
            "product",
            "created_at",
            "user",
            "seller"
        ]

    def create(self, validated_data: dict) -> Request:
        return Request.objects.create(**validated_data)
