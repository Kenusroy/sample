# Generated by Django 5.0.4 on 2024-10-26 01:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0018_finishedworks_state'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookings',
            name='review',
        ),
        migrations.AddField(
            model_name='bookings',
            name='w_status',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
