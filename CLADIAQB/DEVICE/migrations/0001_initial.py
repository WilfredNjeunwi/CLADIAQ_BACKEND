# Generated by Django 5.1.1 on 2024-09-06 09:45

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('USERS', '0008_rename_profileid_organization_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_installed', models.DateTimeField(auto_created=True)),
                ('location', models.CharField(max_length=255)),
                ('organisation_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='USERS.organization')),
            ],
        ),
        migrations.CreateModel(
            name='SensorData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temperature', models.FloatField(null=True)),
                ('humidity', models.FloatField(null=True)),
                ('atm_pressure', models.FloatField(null=True)),
                ('light_intensity', models.FloatField(null=True)),
                ('nh3', models.FloatField(null=True)),
                ('co', models.FloatField(null=True)),
                ('co2', models.FloatField(null=True)),
                ('o3', models.FloatField(null=True)),
                ('c5h5', models.FloatField(null=True)),
                ('cov', models.FloatField(null=True)),
                ('inflamables', models.FloatField(null=True)),
                ('picture', models.ImageField(blank=True, null=True, upload_to='device_pic/')),
                ('time', models.DateTimeField(default=django.utils.timezone.now)),
                ('device_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='DEVICE.device')),
            ],
        ),
    ]
