# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20160315_1532'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='zipcode',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='city',
            name='county',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='city',
            name='latitude',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='city',
            name='longitude',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='city',
            name='name',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='city',
            name='state',
            field=models.ForeignKey(to='main.State', null=True),
        ),
    ]
