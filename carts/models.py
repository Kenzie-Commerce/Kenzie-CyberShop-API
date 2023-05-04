from django.db import models
import uuid


class Cart(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)

    products = models.ManyToManyField(
        "products.Product",
        related_name="carts",
    )

    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="carts",
    )
