# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [('players', '0004_auto_20150501_1048'), ]

    operations = [
        migrations.RemoveField(model_name='historicaldomain',
                               name='population_id', ),
        migrations.RemoveField(model_name='domain',
                               name='population', ),
        migrations.AddField(
            model_name='domain',
            name='population',
            field=models.ManyToManyField(to='players.Population',
                                         blank=True),
            preserve_default=True, ),
    ]
