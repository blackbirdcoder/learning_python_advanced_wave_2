from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator
from django.db import models
from django.conf import settings


class UserModel(AbstractUser):
    class Meta:
        verbose_name = 'client'


class ClientEcommerce(models.Model):
    cash = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        default=0.0,
        validators=[MinValueValidator(0)]
    )
    client = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    class Meta:
        verbose_name = 'Ecommerce'

