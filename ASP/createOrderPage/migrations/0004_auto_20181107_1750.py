# Generated by Django 2.1.3 on 2018-11-07 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('createOrderPage', '0003_auto_20181107_1749'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='deliveredDatetime',
            field=models.DateTimeField(default=None),
        ),
        migrations.AlterField(
            model_name='order',
            name='dispatchedDatetime',
            field=models.DateTimeField(default=None),
        ),
    ]
