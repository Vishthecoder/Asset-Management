# Generated by Django 4.0.4 on 2022-05-10 01:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='asset',
            name='level',
        ),
    ]