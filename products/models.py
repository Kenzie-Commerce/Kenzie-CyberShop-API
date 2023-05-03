from django.db import models
import uuid


class Product(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)

    category = models.CharField(max_length=30)
    name = models.TextField()
    value = models.DecimalField(max_digits=12, decimal_places=2)
    stock = models.IntegerField()
    description = models.TextField(null=True)

    is_avaliable = models.BooleanField(default=True)

    seller_id = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="products",
    )

    class Meta:
        ordering = [
            "name",
        ]
