# Generated by Django 3.1.4 on 2022-07-19 04:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ControlPersonal', '0009_auto_20220718_2328'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cuenta',
            old_name='precio_total',
            new_name='precio',
        ),
        migrations.RemoveField(
            model_name='cuenta',
            name='cantidad',
        ),
        migrations.RemoveField(
            model_name='cuenta',
            name='valor',
        ),
    ]