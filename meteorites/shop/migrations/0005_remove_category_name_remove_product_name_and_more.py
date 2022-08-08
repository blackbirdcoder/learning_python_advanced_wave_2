# Generated by Django 4.0.6 on 2022-08-08 08:35

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_alter_product_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='name',
        ),
        migrations.RemoveField(
            model_name='product',
            name='name',
        ),
        migrations.AddField(
            model_name='category',
            name='title',
            field=models.CharField(max_length=16, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='title',
            field=models.CharField(default='Unknown', max_length=8, null=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='slug_name',
            field=models.SlugField(default='no-category', max_length=20),
        ),
        migrations.AlterField(
            model_name='product',
            name='amount',
            field=models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(default='Unknown', null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='diameter',
            field=models.CharField(default='0x0x0 mm', max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='location',
            field=models.CharField(default='Unknown', max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='slug_name',
            field=models.SlugField(default='no-meteorite', max_length=32),
        ),
        migrations.AlterField(
            model_name='product',
            name='weight',
            field=models.CharField(default='0 g', max_length=8, null=True),
        ),
    ]