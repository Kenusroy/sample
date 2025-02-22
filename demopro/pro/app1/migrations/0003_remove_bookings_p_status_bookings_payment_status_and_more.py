# Generated by Django 5.0.4 on 2024-10-14 07:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_adminsendbookings_w_confirm'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookings',
            name='p_status',
        ),
        migrations.AddField(
            model_name='bookings',
            name='payment_status',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='adminsendbookings',
            name='w_confirm',
            field=models.CharField(choices=[('Accepted', 'Accepted'), ('Rejected', 'Rejected')], default='pending', max_length=15),
        ),
        migrations.CreateModel(
            name='booked',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('phonenumber', models.IntegerField()),
                ('address', models.CharField(max_length=15)),
                ('type', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('pickingdate', models.DateField()),
                ('pickingpoint', models.CharField(max_length=200)),
                ('quantity', models.IntegerField()),
                ('totalprices', models.FloatField()),
                ('location', models.CharField(max_length=100)),
                ('payment_mode', models.CharField(default='Razor_pay', max_length=200, null=True)),
                ('service', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.add_service')),
                ('user_details', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.register')),
            ],
        ),
    ]
