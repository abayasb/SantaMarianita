# Generated by Django 3.1.4 on 2022-07-19 23:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ControlPersonal', '0010_auto_20220718_2341'),
    ]

    operations = [
        migrations.AddField(
            model_name='cuenta',
            name='producto_cuenta',
            field=models.ManyToManyField(to='ControlPersonal.Producto'),
        ),
    ]