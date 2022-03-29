# Generated by Django 4.0.2 on 2022-03-29 05:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sensor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name': 'Sensor',
                'verbose_name_plural': 'Sensores',
                'db_table': 'sensors',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='SensorData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.CharField(max_length=50)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('sensor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sensors.sensor')),
            ],
            options={
                'verbose_name': 'Sensor Data',
                'verbose_name_plural': 'Sensors Data',
                'db_table': 'sensors_data',
                'ordering': ['id'],
            },
        ),
    ]
