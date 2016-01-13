# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0005_auto_20160112_1232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='action',
            name='resolved',
            field=models.CharField(max_length=10, default='UNRESOLVED', choices=[('UNRESOLVED', 'Unresolved'), ('PENDING', 'Pending'), ('RESOLVED', 'Resolved')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='feeding',
            name='resolved',
            field=models.CharField(max_length=10, default='UNRESOLVED', choices=[('UNRESOLVED', 'Unresolved'), ('PENDING', 'Pending'), ('RESOLVED', 'Resolved')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='historicalaction',
            name='resolved',
            field=models.CharField(max_length=10, default='UNRESOLVED', choices=[('UNRESOLVED', 'Unresolved'), ('PENDING', 'Pending'), ('RESOLVED', 'Resolved')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='historicalfeeding',
            name='resolved',
            field=models.CharField(max_length=10, default='UNRESOLVED', choices=[('UNRESOLVED', 'Unresolved'), ('PENDING', 'Pending'), ('RESOLVED', 'Resolved')]),
            preserve_default=True,
        ),
    ]
