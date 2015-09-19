# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vote',
            name='election',
            field=models.ForeignKey(blank=True, to='stats.Election', null=True),
        ),
    ]
