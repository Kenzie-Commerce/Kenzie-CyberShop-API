from users.models import User
from products.models import Product
from django.utils.crypto import get_random_string
from django.core.management.base import BaseCommand, CommandParser


class Command(BaseCommand):
    help = "Create a random products"

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument(
            "-t",
            "--total",
            type=int,
            help="Indicates a quantity of products for creation",
        )

    def handle(self, *args: tuple, **kwargs: dict) -> str | None:
        total = kwargs["total"] or 10

        seller = {
            "username": get_random_string(5),
            "password": "1234",
            "email": f"{get_random_string(4)}@mail.com",
            "is_seller": True,
        }

        user_created = User.objects.create_user(**seller)

        product = {
            "name": "Placa de Vídeo Asus NVIDIA ROG STRIX, RTX 4090, 24 gb gddr6x",
            "value": 10989.99,
            "stock": 50,
            "description": "abc da amazonia",
            "category": "hardware",
            "seller_id": user_created,
        }

        for i in range(total):
            Product.objects.create(**product)

        return f"Products x{total} successfully created!"
