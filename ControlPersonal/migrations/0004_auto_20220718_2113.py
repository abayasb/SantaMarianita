# Generated by Django 3.1.4 on 2022-07-19 02:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ControlPersonal', '0003_auto_20220717_2250'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='cantidad',
        ),
        migrations.RemoveField(
            model_name='producto',
            name='precio_total',
        ),
    ]