# Generated by Django 4.1.5 on 2023-03-28 02:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory_app', '0014_rename_product_id_productstock_product'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='itemstock',
            options={'verbose_name': 'item_stock'},
        ),
        migrations.AlterModelOptions(
            name='productstock',
            options={'verbose_name': 'product_stock'},
        ),
    ]
