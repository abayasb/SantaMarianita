# Generated by Django 3.1.4 on 2022-08-04 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ControlPersonal', '0023_auto_20220804_1345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asistencia',
            name='time_in',
            field=models.TimeField(auto_now_add=True, verbose_name='Hora entrada'),
        ),
        migrations.AlterField(
            model_name='asistencia',
            name='time_out',
            field=models.TimeField(auto_now=True, verbose_name='Hora salida'),
        ),
    ]