# Generated by Django 4.0.6 on 2022-08-16 13:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ClientProfileModel',
            new_name='ClientEcommerce',
        ),
        migrations.AlterModelOptions(
            name='clientecommerce',
            options={'verbose_name': 'Ecommerce'},
        ),
        migrations.AlterModelOptions(
            name='usermodel',
            options={'verbose_name': 'client'},
        ),
    ]