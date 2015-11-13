# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0006_auto_20150919_1928'),
    ]

    operations = [
        migrations.AlterField(
            model_name='election',
            name='type',
            field=models.CharField(default=None, max_length=63, null=True, blank=True),
        ),
    ]
