# Generated by Django 5.0.4 on 2024-10-26 01:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0020_remove_adminsendbookings_w_status_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='adminsendbookings',
            name='cl_status',
        ),
    ]