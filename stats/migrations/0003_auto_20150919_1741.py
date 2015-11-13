# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0002_auto_20150919_1109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='election',
            name='address',
            field=models.CharField(default=None, max_length=500, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='election',
            name='commune',
            field=models.CharField(default=None, max_length=200, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='election',
            name='district',
            field=models.CharField(default=None, max_length=50, null=True, blank=True),
        ),
    ]
