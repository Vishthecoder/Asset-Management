# Generated by Django 4.0.1 on 2022-01-21 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0003_alter_assetmaintenance_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='asset',
            name='image',
            field=models.ImageField(default='index.jpg', upload_to='AssetImages/'),
        ),
    ]