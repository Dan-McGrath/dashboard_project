# Generated by Django 4.1.5 on 2023-04-05 04:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory_app', '0020_alter_product_items_unique_together'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product_items',
            name='id',
        ),
        migrations.AlterField(
            model_name='product_items',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='inventory_app.product'),
        ),
    ]
