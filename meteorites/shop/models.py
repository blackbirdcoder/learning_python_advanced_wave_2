from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Category(models.Model):
    slug_name = models.SlugField(max_length=32, null=True)
    name = models.CharField(max_length=32, null=True)
    description = models.TextField(null=True)

    def __str__(self):
        return f'{self.slug_name} {self.name} {self.description}'


class Product(models.Model):
    slug_name = models.SlugField(max_length=32, null=True)
    description = models.TextField(null=True)
    amount = models.IntegerField(default=1, validators=[MaxValueValidator(10), MinValueValidator(1)])
    weight = models.CharField(max_length=32, null=True)
    location = models.CharField(max_length=64, null=True)
    name = models.CharField(max_length=5, null=True)
    price = models.DecimalField(max_digits=9, decimal_places=2, default=0, validators=[MinValueValidator(0)])
    diameter = models.CharField(max_length=25, null=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.name} {self.description} {self.category}'
