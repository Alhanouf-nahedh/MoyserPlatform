# Generated by Django 5.1.4 on 2024-12-18 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account_app', '0009_disabilityuser_address_disabilityuser_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companion',
            name='certification',
            field=models.FileField(null=True, upload_to='pdf/'),
        ),
    ]
