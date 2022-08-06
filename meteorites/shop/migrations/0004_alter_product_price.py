# Generated by Django 4.0.6 on 2022-08-06 21:56

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_alter_product_amount_alter_product_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=9, validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]
