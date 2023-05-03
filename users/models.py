from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid


# Create your models here.
class User(AbstractUser):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)

    email = models.EmailField(max_length=127, unique=True)

    is_superuser = models.BooleanField(default=False, null=True)
    is_seller = models.BooleanField(default=False, null=True)
