# Generated by Django 2.1.3 on 2018-11-07 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0011_auto_20181107_1556'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='CMid',
        ),
        migrations.AlterField(
            model_name='order',
            name='deliveredDatetime',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='dispatchedDatetime',
            field=models.DateTimeField(blank=True),
        ),
    ]
