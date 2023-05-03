from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "email", "username", "password", "is_superuser", "is_seller"]
        extra_kwargs = {
            "email": {
                "validators": [
                    UniqueValidator(
                        queryset=User.objects.all(),
                        message="This field must be unique.",
                    )
                ]
            },
            "password": {"write_only": True},
            "username": {
                "validators": [
                    UniqueValidator(
                        queryset=User.objects.all(),
                        message="A user with that username already exists.",
                    )
                ]
            },
        }

        def create(self, validated_data: dict) -> User:
            if validated_data["is_superuser"]:
                return User.objects.create_superuser(**validated_data)
            else:
                return User.objects.create_user(**validated_data)

        def update(self, instance: User, validated_data: dict):
            instance.set_password(validated_data.get("password"))
            instance.is_seller = validated_data.get("is_seller", instance.is_seller)

            instance.save()
            return instance
