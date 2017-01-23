# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [('players', '0006_auto_20160113_1806'), ]

    operations = [
        migrations.AlterField(model_name='domain',
                              name='influence',
                              field=models.CharField(max_length=200),
                              preserve_default=True, ),
        migrations.AlterField(model_name='domain',
                              name='masquerade',
                              field=models.CharField(max_length=200),
                              preserve_default=True, ),
        migrations.AlterField(model_name='domain',
                              name='status',
                              field=models.CharField(max_length=200),
                              preserve_default=True, ),
        migrations.AlterField(model_name='historicaldomain',
                              name='influence',
                              field=models.CharField(max_length=200),
                              preserve_default=True, ),
        migrations.AlterField(model_name='historicaldomain',
                              name='masquerade',
                              field=models.CharField(max_length=200),
                              preserve_default=True, ),
        migrations.AlterField(model_name='historicaldomain',
                              name='status',
                              field=models.CharField(max_length=200),
                              preserve_default=True, ),
    ]
