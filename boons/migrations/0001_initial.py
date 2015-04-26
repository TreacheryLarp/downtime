# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0003_auto_20150425_1242'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Boon',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('is_activated', models.BooleanField(default=False)),
                ('description', models.TextField()),
                ('creditor', models.ForeignKey(to='players.Character', related_name='debits')),
                ('debtor', models.ForeignKey(to='players.Character', related_name='credits')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='BoonSize',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('value', models.PositiveIntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='HistoricalBoon',
            fields=[
                ('id', models.IntegerField(verbose_name='ID', blank=True, db_index=True, auto_created=True)),
                ('is_activated', models.BooleanField(default=False)),
                ('debtor_id', models.IntegerField(blank=True, db_index=True, null=True)),
                ('creditor_id', models.IntegerField(blank=True, db_index=True, null=True)),
                ('size_id', models.IntegerField(blank=True, db_index=True, null=True)),
                ('description', models.TextField()),
                ('history_id', models.AutoField(serialize=False, primary_key=True)),
                ('history_date', models.DateTimeField()),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'ordering': ('-history_date', '-history_id'),
                'verbose_name': 'historical boon',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='HistoricalBoonSize',
            fields=[
                ('id', models.IntegerField(verbose_name='ID', blank=True, db_index=True, auto_created=True)),
                ('name', models.CharField(max_length=200)),
                ('value', models.PositiveIntegerField()),
                ('history_id', models.AutoField(serialize=False, primary_key=True)),
                ('history_date', models.DateTimeField()),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'ordering': ('-history_date', '-history_id'),
                'verbose_name': 'historical boon size',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='boon',
            name='size',
            field=models.ForeignKey(to='boons.BoonSize'),
            preserve_default=True,
        ),
    ]
