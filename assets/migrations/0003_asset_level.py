# Generated by Django 4.0.4 on 2022-05-10 01:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0002_remove_asset_level'),
    ]

    operations = [
        migrations.AddField(
            model_name='asset',
            name='level',
            field=models.CharField(choices=[('Level I', '1'), ('Level II', '2'), ('Level III', '3')], default='1', max_length=30),
        ),
    ]
