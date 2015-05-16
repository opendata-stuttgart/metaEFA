# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20150516_1411'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='station',
            name='id',
        ),
        migrations.AlterField(
            model_name='station',
            name='station_id',
            field=models.TextField(primary_key=True, serialize=False),
        ),
    ]
