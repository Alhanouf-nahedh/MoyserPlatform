# Generated by Django 5.1.4 on 2024-12-16 15:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_feedback_booking_feedback_companion_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feedback',
            name='booking',
        ),
    ]
