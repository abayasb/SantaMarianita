# Generated by Django 3.1.4 on 2022-09-04 02:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ControlPersonal', '0025_remove_asistencia_number_hour'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asistencia',
            name='date',
            field=models.DateField(auto_now=True, verbose_name='Fecha'),
        ),
        migrations.AlterField(
            model_name='asistencia',
            name='time_in',
            field=models.TimeField(auto_now=True, verbose_name='Hora entrada'),
        ),
    ]
