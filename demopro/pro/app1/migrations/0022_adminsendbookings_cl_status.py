# Generated by Django 5.0.4 on 2024-10-26 01:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0021_remove_adminsendbookings_cl_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='adminsendbookings',
            name='cl_status',
            field=models.CharField(choices=[('Cancelled', 'Cancelled')], default='pending', max_length=15),
        ),
    ]
