# Generated by Django 2.0.5 on 2018-05-14 12:34

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_auto_20180511_1344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='created_at',
            field=models.DateField(blank=True, null=True, verbose_name=datetime.datetime(2018, 5, 14, 12, 34, 10, 85453, tzinfo=utc)),
        ),
    ]
