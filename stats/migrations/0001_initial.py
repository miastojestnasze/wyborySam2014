# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.CharField(default=None, max_length=63)),
                ('surname', models.CharField(default=None, max_length=255)),
                ('names', models.CharField(default=None, max_length=255)),
                ('age', models.IntegerField(default=0)),
                ('sex', models.CharField(default=None, max_length=3)),
                ('place_of_living', models.CharField(default=None, max_length=511)),
                ('voivodeship', models.CharField(default=None, max_length=127)),
                ('nationality', models.CharField(default=None, max_length=127)),
                ('votes', models.IntegerField(default=0)),
                ('election_committee', models.CharField(default=None, max_length=63)),
                ('number_of_list', models.IntegerField(default=0)),
                ('pos', models.IntegerField(default=0)),
                ('number_of_district', models.IntegerField(default=0)),
                ('grade', models.CharField(default=None, max_length=10)),
                ('mandate', models.CharField(default=b'n', max_length=2)),
                ('supported_by', models.TextField(default=None)),
                ('teryt', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Election',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('teryt', models.IntegerField(default=0)),
                ('territory', models.CharField(max_length=7)),
                ('number_of_district', models.IntegerField(default=0)),
                ('address', models.CharField(default=None, max_length=500)),
                ('district', models.CharField(default=None, max_length=50)),
                ('commune', models.CharField(default=None, max_length=200)),
                ('commune_type', models.CharField(default=None, max_length=200)),
                ('county', models.CharField(default=None, max_length=200)),
                ('voivodeship', models.CharField(default=None, max_length=200)),
                ('number_of_electoral_circuit', models.IntegerField(default=0)),
                ('number_electoral_circuits', models.IntegerField(default=0)),
                ('type', models.CharField(default=None, max_length=63)),
                ('number_of_voters', models.IntegerField(default=0)),
                ('number_of_proxies', models.IntegerField(default=0)),
                ('cards_given', models.IntegerField(default=0)),
                ('cards_taken', models.IntegerField(default=0)),
                ('cards_taken_from_box', models.IntegerField(default=0)),
                ('votes_valid', models.IntegerField(default=0)),
                ('votes_invalid', models.IntegerField(default=0)),
                ('cards_received', models.IntegerField(default=0)),
                ('cards_valid', models.IntegerField(default=0)),
                ('cards_invalid', models.IntegerField(default=0)),
                ('cards_invalid_x', models.IntegerField(default=0)),
                ('cards_invalid_xx', models.IntegerField(default=0)),
                ('cards_unused', models.IntegerField(default=0)),
                ('polish_citizens', models.IntegerField(default=0)),
                ('polish_citizens_b', models.IntegerField(default=0)),
                ('envelope_unsealed', models.IntegerField(default=0)),
                ('envelopes_thrown_into_box', models.IntegerField(default=0)),
                ('envelopes_without_statement', models.IntegerField(default=0)),
                ('envelopes_returned', models.IntegerField(default=0)),
                ('envelopes_returned_without_envelope', models.IntegerField(default=0)),
                ('unsigned_statements', models.IntegerField(default=0)),
                ('eu_citizens', models.IntegerField(default=0)),
                ('eu_citiznes_b', models.IntegerField(default=0)),
                ('electoral_packages', models.IntegerField(default=0)),
                ('election_type', models.CharField(default=None, max_length=10)),
                ('notes', models.TextField(default=b'[]')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('political_party', models.CharField(default=None, max_length=2047)),
                ('amount', models.IntegerField(default=0)),
                ('election', models.ForeignKey(to='stats.Election')),
            ],
        ),
    ]
