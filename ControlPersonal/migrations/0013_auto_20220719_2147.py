# Generated by Django 3.1.4 on 2022-07-20 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ControlPersonal', '0012_auto_20220719_1949'),
    ]

    operations = [
        migrations.AddField(
            model_name='cuenta',
            name='cantidad',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='cuenta',
            name='valor',
            field=models.FloatField(default=0),
        ),
    ]
