# Generated by Django 3.1.4 on 2022-07-19 04:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ControlPersonal', '0007_auto_20220718_2315'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='producto_proveedor',
        ),
        migrations.AddField(
            model_name='producto',
            name='proveedor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='ControlPersonal.proveedor'),
        ),
    ]