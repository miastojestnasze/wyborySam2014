# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0005_auto_20150919_1832'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='supported_by',
            field=models.TextField(default=None, null=True, blank=True),
        ),
    ]
