# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0004_auto_20150919_1748'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='candidate',
            name='type',
        ),
        migrations.AddField(
            model_name='candidate',
            name='election_type',
            field=models.CharField(default=None, max_length=511),
        ),
        migrations.AlterField(
            model_name='election',
            name='election_type',
            field=models.CharField(default=None, max_length=511),
        ),
    ]
