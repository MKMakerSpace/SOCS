# Generated by Django 3.0.6 on 2021-05-18 20:44

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AssetList',
            fields=[
                ('AssetID', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('Name', models.CharField(help_text='Item Name', max_length=50)),
                ('Manufacturer', models.CharField(help_text='Manufacturer Name', max_length=50)),
                ('Model', models.CharField(help_text='Manufacturer Model', max_length=50)),
                ('SerialNo', models.CharField(help_text='Model Serial Number', max_length=50)),
                ('Location', models.CharField(help_text='Location Stored/Kept in space', max_length=50)),
                ('Description', models.CharField(help_text='Item Description', max_length=200)),
                ('Notes', models.CharField(help_text='Item Notes', max_length=200)),
                ('PurchasePrice', models.DecimalField(decimal_places=2, help_text='Price to purchase/replace the item.', max_digits=9)),
                ('Value', models.DecimalField(decimal_places=2, help_text='Current value of the item', max_digits=9)),
                ('DateAcquired', models.DateField(help_text='Date item was acquired.')),
                ('Status', models.CharField(help_text='Current Status of the item.', max_length=50)),
                ('Warranty', models.DecimalField(decimal_places=3, help_text='Manufacturer Warranty Period', max_digits=3)),
            ],
            options={
                'ordering': ['Manufacturer', 'Model'],
            },
        ),
    ]
