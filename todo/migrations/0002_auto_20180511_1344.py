# Generated by Django 2.0.5 on 2018-05-11 12:44

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='created_at',
            field=models.DateField(blank=True, null=True, verbose_name=datetime.datetime(2018, 5, 11, 12, 44, 25, 29252, tzinfo=utc)),
        ),
    ]
