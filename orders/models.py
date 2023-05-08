from django.db import models
import uuid


class Status(models.TextChoices):
    ORDER_PLACED = ("Order placed",)
    IN_PROGRESS = ("In progress",)
    DELIVERED = "Delivered"


# Create your models here.
class Order(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)

    product = models.ForeignKey(
        "products.Product", on_delete=models.CASCADE, related_name="orders"
    )

    status = models.CharField(
        max_length=20, choices=Status.choices, default=Status.ORDER_PLACED
    )
    created_at = models.DateTimeField(auto_now_add=True)

    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="orders"
    )
    seller = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="orders_received"
    )
