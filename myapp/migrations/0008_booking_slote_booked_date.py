# Generated by Django 5.0.7 on 2024-07-30 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_alter_add_appointment_user_booked'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking_slote',
            name='booked_date',
            field=models.DateTimeField(null=True),
        ),
    ]
