from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Category(models.Model):
    slug_name = models.SlugField(max_length=20, null=True)
    title = models.CharField(max_length=16, null=True)
    description = models.TextField(null=True)

    def __str__(self):
        return f'{self.slug_name} {self.title} {self.description}'


class Product(models.Model):
    slug_name = models.SlugField(max_length=32, null=True)
    description = models.TextField(null=True, default='Unknown')
    amount = models.IntegerField(default=1, validators=[MaxValueValidator(10), MinValueValidator(0)])
    weight = models.CharField(max_length=8, null=True, default='0 g')
    location = models.CharField(max_length=64, null=True, default='Unknown')
    title = models.CharField(max_length=8, null=True, default='Unknown')
    price = models.DecimalField(max_digits=9, decimal_places=2, default=0, validators=[MinValueValidator(0)])
    diameter = models.CharField(max_length=25, null=True, default='not specified')
    category = models.ForeignKey(Category, on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.title} {self.description} {self.category}'
