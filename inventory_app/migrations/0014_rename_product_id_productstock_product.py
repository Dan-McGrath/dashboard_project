# Generated by Django 4.1.5 on 2023-03-27 23:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory_app', '0013_rename_current_count_productstock_product_count'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productstock',
            old_name='product_id',
            new_name='product',
        ),
    ]