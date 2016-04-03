# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [('players', '0003_auto_20150425_1242'), ]

    operations = [
        migrations.AddField(model_name='extraaction',
                            name='description',
                            field=models.TextField(default=''),
                            preserve_default=False, ),
        migrations.AddField(model_name='historicalextraaction',
                            name='description',
                            field=models.TextField(default=''),
                            preserve_default=False, ),
        migrations.AlterField(model_name='extraaction',
                              name='character',
                              field=models.ForeignKey(related_name='+',
                                                      to='players.Character'),
                              preserve_default=True, ),
        migrations.AlterField(model_name='extraaction',
                              name='session',
                              field=models.ForeignKey(related_name='+',
                                                      to='players.Session'),
                              preserve_default=True, ),
    ]
