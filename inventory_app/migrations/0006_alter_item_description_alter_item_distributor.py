# Generated by Django 4.1.5 on 2023-02-02 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory_app', '0005_alter_item_description_alter_item_distributor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='description',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='item',
            name='distributor',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
