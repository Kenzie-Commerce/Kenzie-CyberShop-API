from django.db import models


# Create your models here.
class Address(models.Model):
    street = models.CharField(max_length=50)
    number = models.CharField(max_length=8)
    complement = models.TextField(null=True)
    district = models.CharField(max_length=50)
    user = models.ForeignKey(
        "users.User",
        related_name="Addresses",
        on_delete=models.CASCADE,
    )
