# Generated by Django 5.0.4 on 2024-10-08 05:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='add_location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='add_service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=15)),
                ('price', models.IntegerField()),
                ('image', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='complaint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=50)),
                ('message', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='driverreg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('profile', models.FileField(upload_to='pdfs')),
                ('cv', models.FileField(upload_to='pdfs')),
                ('phonenumber', models.IntegerField()),
                ('gender', models.CharField(choices=[('a', 'male'), ('b', 'female')], max_length=10)),
                ('address', models.CharField(max_length=15)),
                ('joiningdate', models.DateField()),
                ('licensenumber', models.CharField(max_length=15)),
                ('location', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=10)),
                ('c_password', models.CharField(max_length=10)),
                ('status', models.CharField(choices=[('free', 'free'), ('In work', 'In work'), ('Off Duty', 'Off Duty')], default='Off Duty', max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=10, unique=True)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.CharField(max_length=15)),
                ('phonenumber', models.IntegerField()),
                ('password', models.CharField(max_length=10)),
                ('cpassword', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='passwordreset',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(max_length=4)),
                ('emp', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.driverreg')),
                ('users', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.register')),
            ],
        ),
        migrations.CreateModel(
            name='bookings',
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
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('accepted', 'Accepted'), ('Cancelled', 'Cancelled')], default='pending', max_length=15)),
                ('p_status', models.CharField(choices=[('cash paid', 'cash paid'), ('cash not paid', 'cash not paid')], default='cash not paid', max_length=15)),
                ('payment_mode', models.CharField(default='Razor_pay', max_length=200, null=True)),
                ('service', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.add_service')),
                ('user_details', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.register')),
            ],
        ),
        migrations.CreateModel(
            name='adminsendbookings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('type', models.CharField(max_length=100)),
                ('quantity', models.IntegerField()),
                ('price', models.IntegerField()),
                ('phonenumber', models.IntegerField()),
                ('address', models.CharField(max_length=15)),
                ('pickingdate', models.DateField()),
                ('city', models.CharField(max_length=50)),
                ('landmark', models.CharField(max_length=15)),
                ('w_status', models.CharField(choices=[('Pending', 'Pending'), ('Finished', 'Finished'), ('Cancelled', 'Cancelled')], default='pending', max_length=15)),
                ('emp_details', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.driverreg')),
                ('user_details', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.register')),
            ],
        ),
    ]
