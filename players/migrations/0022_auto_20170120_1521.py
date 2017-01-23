# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2017-01-20 15:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0021_auto_20170120_1431'),
    ]

    operations = [
        migrations.RenameField(
            model_name='learnspecialization',
            old_name='newSpecialization',
            new_name='new_specialization',
        ),
        migrations.RenameField(
            model_name='learnspecialization',
            old_name='oldSpecialization',
            new_name='old_specialization',
        ),
        migrations.AlterField(
            model_name='investigatecharacterdowntimeactions',
            name='target',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='investigate_downtime_actions', to='players.Character'),
        ),
        migrations.AlterField(
            model_name='investigatecharacterinfluence',
            name='target',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='investigate_influence', to='players.Character'),
        ),
        migrations.AlterField(
            model_name='investigatecharacterresources',
            name='target',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='investigate_resources', to='players.Character'),
        ),
    ]
