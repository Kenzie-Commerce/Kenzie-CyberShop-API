from django.db import models


class Product(models.Model):
    category = models.CharField(max_length=30)
    name = models.TextField()
    value = models.DecimalField(max_digits=12, decimal_places=2)
    stock = models.IntegerField(max_length=1000)
    description = models.TextField(null=True)

    is_avaliable = models.BooleanField(default=True)

    seller_id = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="products",
    )
