# Generated by Django 5.0.7 on 2024-07-31 13:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_add_complaints'),
    ]

    operations = [
        migrations.CreateModel(
            name='Add_feedbacks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, null=True)),
                ('feedback', models.CharField(max_length=500, null=True)),
                ('posted_date', models.DateTimeField(null=True)),
                ('doctor_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.add_doctors')),
                ('user_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.user_registration')),
            ],
        ),
    ]
