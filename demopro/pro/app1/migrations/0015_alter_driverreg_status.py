# Generated by Django 5.0.4 on 2024-10-25 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0014_adminsendbookings_district_adminsendbookings_state_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driverreg',
            name='status',
            field=models.CharField(choices=[('free', 'free'), ('In work', 'In work'), ('Off Duty', 'Off Duty')], default='free', max_length=15),
        ),
    ]
