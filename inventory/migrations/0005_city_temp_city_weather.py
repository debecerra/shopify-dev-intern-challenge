# Generated by Django 4.0.4 on 2022-05-11 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0004_rename_location_inventoryitem_warehouse_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='temp',
            field=models.DecimalField(decimal_places=1, default=0.0, max_digits=4),
        ),
        migrations.AddField(
            model_name='city',
            name='weather',
            field=models.CharField(default='no weather info to display', max_length=50),
        ),
    ]
