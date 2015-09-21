# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0007_auto_20150919_1932'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='election_committee',
            field=models.CharField(default=None, max_length=2047),
        ),
    ]
