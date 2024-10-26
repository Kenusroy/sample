# Generated by Django 5.0.4 on 2024-10-26 01:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0019_remove_bookings_review_bookings_w_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='adminsendbookings',
            name='w_status',
        ),
        migrations.AddField(
            model_name='adminsendbookings',
            name='cl_status',
            field=models.CharField(choices=[('Cancelled', 'Cancelled')], default='pending', max_length=15),
        ),
    ]
