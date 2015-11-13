# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0003_auto_20150919_1741'),
    ]

    operations = [
        migrations.AlterField(
            model_name='election',
            name='commune_type',
            field=models.CharField(default=None, max_length=200, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='election',
            name='county',
            field=models.CharField(default=None, max_length=200, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='election',
            name='number_electoral_circuits',
            field=models.IntegerField(default=0, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='election',
            name='voivodeship',
            field=models.CharField(default=None, max_length=200, null=True, blank=True),
        ),
    ]
