# Generated by Django 2.0.5 on 2018-05-15 11:28

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0014_auto_20180515_0948'),
    ]

    operations = [
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='todo',
            name='created_at',
            field=models.DateField(blank=True, null=True, verbose_name=datetime.datetime(2018, 5, 15, 11, 28, 49, 321276, tzinfo=utc)),
        ),
    ]
