# Generated by Django 5.0.7 on 2024-07-29 18:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_rename_user_booked_booking_slote_booked'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking_slote',
            old_name='booked',
            new_name='user_booked',
        ),
    ]