# Generated by Django 4.0.1 on 2022-01-21 02:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asset',
            name='rfid',
            field=models.CharField(max_length=8, unique=True),
        ),
        migrations.AlterField(
            model_name='asset',
            name='serial_no',
            field=models.CharField(max_length=10, unique=True),
        ),
        migrations.CreateModel(
            name='AssetMaintenance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('maintenance_id', models.CharField(max_length=10, unique=True)),
                ('maintenance_date', models.DateField()),
                ('maintenance_description', models.TextField()),
                ('maintenance_cost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('performed_by', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('asset_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='assets.asset')),
            ],
        ),
    ]
