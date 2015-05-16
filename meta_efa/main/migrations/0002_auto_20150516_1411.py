# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='station',
            name='full_name',
            field=models.TextField(default='changeme'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='station',
            name='station_id',
            field=models.TextField(default='changeme'),
            preserve_default=False,
        ),
    ]
