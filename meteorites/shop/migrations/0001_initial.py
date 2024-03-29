# Generated by Django 4.0.6 on 2022-08-16 11:38

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug_name', models.SlugField(max_length=20, null=True)),
                ('title', models.CharField(max_length=16, null=True)),
                ('description', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug_name', models.SlugField(max_length=32, null=True)),
                ('description', models.TextField(default='Unknown', null=True)),
                ('amount', models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(0)])),
                ('weight', models.CharField(default='0 g', max_length=8, null=True)),
                ('location', models.CharField(default='Unknown', max_length=64, null=True)),
                ('title', models.CharField(default='Unknown', max_length=8, null=True)),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=9, validators=[django.core.validators.MinValueValidator(0)])),
                ('diameter', models.CharField(default='not specified', max_length=25, null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='shop.category')),
            ],
        ),
    ]
