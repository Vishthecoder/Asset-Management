# Generated by Django 4.0.3 on 2022-03-26 01:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0007_rename_acquisition_date_asset_purchase_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='asset',
            name='id',
        ),
        migrations.AlterField(
            model_name='asset',
            name='rfid',
            field=models.CharField(max_length=10, primary_key=True, serialize=False, unique=True),
        ),
    ]