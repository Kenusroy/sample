# Generated by Django 5.0.4 on 2024-10-09 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='adminsendbookings',
            name='w_confirm',
            field=models.CharField(choices=[('Accepted', 'Accepted'), ('Rejected', 'Rejected')], default=1, max_length=15),
            preserve_default=False,
        ),
    ]
