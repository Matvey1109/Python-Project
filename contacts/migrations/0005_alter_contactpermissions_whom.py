# Generated by Django 3.2.6 on 2021-08-23 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0004_auto_20210823_1834'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactpermissions',
            name='whom',
            field=models.CharField(max_length=100),
        ),
    ]
