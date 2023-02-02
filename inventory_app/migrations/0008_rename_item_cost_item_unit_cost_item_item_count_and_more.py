# Generated by Django 4.1.5 on 2023-02-02 21:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory_app', '0007_remove_item_serial_number_item_item_cost_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='item_cost',
            new_name='unit_cost',
        ),
        migrations.AddField(
            model_name='item',
            name='item_count',
            field=models.IntegerField(default=0),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0)),
                ('total_cost', models.DecimalField(decimal_places=2, default=0.0, max_digits=6)),
                ('item_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory_app.item')),
            ],
        ),
    ]
