# Generated by Django 3.1.1 on 2021-03-25 06:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('metroevent', '0005_auto_20210325_1325'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='administrator',
            table='Administrator',
        ),
        migrations.AlterModelTable(
            name='organizer',
            table='Organizer',
        ),
    ]
