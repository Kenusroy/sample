# Generated by Django 5.0.4 on 2024-10-15 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_remove_bookings_p_status_bookings_payment_status_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookings',
            name='review',
            field=models.CharField(choices=[('poor', 'poor'), ('Average', 'Average'), ('Excelent', 'Excelent')], default=1, max_length=15),
            preserve_default=False,
        ),
    ]
