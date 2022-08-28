# Generated by Django 3.1.4 on 2022-07-18 03:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ControlPersonal', '0002_auto_20220717_2148'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='fecha_adquisicion',
            field=models.DateField(auto_now_add=True, default=datetime.date(2022, 7, 17)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='producto',
            name='cantidad',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='producto',
            name='precio_total',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='producto',
            name='precio_unitario',
            field=models.FloatField(default=0),
        ),
    ]