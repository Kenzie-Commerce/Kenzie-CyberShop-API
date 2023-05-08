import uuid
from django.db import models


# Create your models here.
class Address(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)

    street = models.CharField(max_length=50)
    number = models.CharField(max_length=8)
    complement = models.TextField(null=True)
    district = models.CharField(max_length=50)
    default = models.BooleanField(default=False)

    user = models.ForeignKey(
        "users.User",
        related_name="addresses",
        on_delete=models.CASCADE,
    )
