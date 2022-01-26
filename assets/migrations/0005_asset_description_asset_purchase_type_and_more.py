# Generated by Django 4.0.1 on 2022-01-26 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0004_asset_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='asset',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='asset',
            name='purchase_type',
            field=models.CharField(choices=[('None', 'None'), ('Owned', 'Owned'), ('Subscription', 'Subscription')], default='None', max_length=30),
        ),
        migrations.AddField(
            model_name='asset',
            name='warranty_expiry',
            field=models.DateField(null=True),
        ),
    ]