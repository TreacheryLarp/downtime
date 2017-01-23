# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Action',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('description', models.TextField()),
                ('resolved', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ActionOption',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('count', models.PositiveIntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ActionType',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=200)),
                ('template', models.TextField(blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ActiveDisciplines',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Age',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=200)),
                ('action_options', models.ManyToManyField(to='players.ActionOption', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=200)),
                ('resources', models.PositiveIntegerField()),
                ('age', models.ForeignKey(to='players.Age')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Clan',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Discipline',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Domain',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=200)),
                ('feeding_capacity', models.PositiveIntegerField()),
                ('status', models.TextField()),
                ('influence', models.TextField()),
                ('masquerade', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ExtraAction',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('action_options', models.ManyToManyField(to='players.ActionOption')),
                ('character', models.ForeignKey(to='players.Character')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Feeding',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('feeding_points', models.PositiveIntegerField()),
                ('description', models.TextField()),
                ('resolved', models.BooleanField(default=False)),
                ('character', models.ForeignKey(to='players.Character')),
                ('discipline', models.ForeignKey(to='players.Discipline')),
                ('domain', models.ForeignKey(to='players.Domain')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='HistoricalAction',
            fields=[
                ('id', models.IntegerField(db_index=True, verbose_name='ID', blank=True, auto_created=True)),
                ('action_type_id', models.IntegerField(null=True, db_index=True, blank=True)),
                ('character_id', models.IntegerField(null=True, db_index=True, blank=True)),
                ('session_id', models.IntegerField(null=True, db_index=True, blank=True)),
                ('description', models.TextField()),
                ('resolved', models.BooleanField(default=False)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_type', models.CharField(max_length=1, choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')])),
                ('history_user', models.ForeignKey(null=True, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-history_date', '-history_id'),
                'verbose_name': 'historical action',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='HistoricalActionOption',
            fields=[
                ('id', models.IntegerField(db_index=True, verbose_name='ID', blank=True, auto_created=True)),
                ('count', models.PositiveIntegerField()),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_type', models.CharField(max_length=1, choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')])),
                ('history_user', models.ForeignKey(null=True, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-history_date', '-history_id'),
                'verbose_name': 'historical action option',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='HistoricalActionType',
            fields=[
                ('id', models.IntegerField(db_index=True, verbose_name='ID', blank=True, auto_created=True)),
                ('name', models.CharField(max_length=200)),
                ('template', models.TextField(blank=True)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_type', models.CharField(max_length=1, choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')])),
                ('history_user', models.ForeignKey(null=True, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-history_date', '-history_id'),
                'verbose_name': 'historical action type',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='HistoricalActiveDisciplines',
            fields=[
                ('id', models.IntegerField(db_index=True, verbose_name='ID', blank=True, auto_created=True)),
                ('character_id', models.IntegerField(null=True, db_index=True, blank=True)),
                ('session_id', models.IntegerField(null=True, db_index=True, blank=True)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_type', models.CharField(max_length=1, choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')])),
                ('history_user', models.ForeignKey(null=True, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-history_date', '-history_id'),
                'verbose_name': 'historical active disciplines',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='HistoricalAge',
            fields=[
                ('id', models.IntegerField(db_index=True, verbose_name='ID', blank=True, auto_created=True)),
                ('name', models.CharField(max_length=200)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_type', models.CharField(max_length=1, choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')])),
                ('history_user', models.ForeignKey(null=True, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-history_date', '-history_id'),
                'verbose_name': 'historical age',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='HistoricalCharacter',
            fields=[
                ('id', models.IntegerField(db_index=True, verbose_name='ID', blank=True, auto_created=True)),
                ('name', models.CharField(max_length=200)),
                ('user_id', models.IntegerField(null=True, db_index=True, blank=True)),
                ('age_id', models.IntegerField(null=True, db_index=True, blank=True)),
                ('resources', models.PositiveIntegerField()),
                ('clan_id', models.IntegerField(null=True, db_index=True, blank=True)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_type', models.CharField(max_length=1, choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')])),
                ('history_user', models.ForeignKey(null=True, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-history_date', '-history_id'),
                'verbose_name': 'historical character',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='HistoricalClan',
            fields=[
                ('id', models.IntegerField(db_index=True, verbose_name='ID', blank=True, auto_created=True)),
                ('name', models.CharField(max_length=200)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_type', models.CharField(max_length=1, choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')])),
                ('history_user', models.ForeignKey(null=True, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-history_date', '-history_id'),
                'verbose_name': 'historical clan',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='HistoricalDiscipline',
            fields=[
                ('id', models.IntegerField(db_index=True, verbose_name='ID', blank=True, auto_created=True)),
                ('name', models.CharField(max_length=200)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_type', models.CharField(max_length=1, choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')])),
                ('history_user', models.ForeignKey(null=True, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-history_date', '-history_id'),
                'verbose_name': 'historical discipline',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='HistoricalDomain',
            fields=[
                ('id', models.IntegerField(db_index=True, verbose_name='ID', blank=True, auto_created=True)),
                ('name', models.CharField(max_length=200)),
                ('feeding_capacity', models.PositiveIntegerField()),
                ('status', models.TextField()),
                ('influence', models.TextField()),
                ('masquerade', models.TextField()),
                ('population_id', models.IntegerField(null=True, db_index=True, blank=True)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_type', models.CharField(max_length=1, choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')])),
                ('history_user', models.ForeignKey(null=True, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-history_date', '-history_id'),
                'verbose_name': 'historical domain',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='HistoricalExtraAction',
            fields=[
                ('id', models.IntegerField(db_index=True, verbose_name='ID', blank=True, auto_created=True)),
                ('character_id', models.IntegerField(null=True, db_index=True, blank=True)),
                ('session_id', models.IntegerField(null=True, db_index=True, blank=True)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_type', models.CharField(max_length=1, choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')])),
                ('history_user', models.ForeignKey(null=True, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-history_date', '-history_id'),
                'verbose_name': 'historical extra action',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='HistoricalFeeding',
            fields=[
                ('id', models.IntegerField(db_index=True, verbose_name='ID', blank=True, auto_created=True)),
                ('character_id', models.IntegerField(null=True, db_index=True, blank=True)),
                ('session_id', models.IntegerField(null=True, db_index=True, blank=True)),
                ('domain_id', models.IntegerField(null=True, db_index=True, blank=True)),
                ('feeding_points', models.PositiveIntegerField()),
                ('discipline_id', models.IntegerField(null=True, db_index=True, blank=True)),
                ('description', models.TextField()),
                ('resolved', models.BooleanField(default=False)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_type', models.CharField(max_length=1, choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')])),
                ('history_user', models.ForeignKey(null=True, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-history_date', '-history_id'),
                'verbose_name': 'historical feeding',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='HistoricalInfluence',
            fields=[
                ('id', models.IntegerField(db_index=True, verbose_name='ID', blank=True, auto_created=True)),
                ('name', models.CharField(max_length=200)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_type', models.CharField(max_length=1, choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')])),
                ('history_user', models.ForeignKey(null=True, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-history_date', '-history_id'),
                'verbose_name': 'historical influence',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='HistoricalInfluenceRating',
            fields=[
                ('id', models.IntegerField(db_index=True, verbose_name='ID', blank=True, auto_created=True)),
                ('influence_id', models.IntegerField(null=True, db_index=True, blank=True)),
                ('rating', models.PositiveIntegerField()),
                ('character_id', models.IntegerField(null=True, db_index=True, blank=True)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_type', models.CharField(max_length=1, choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')])),
                ('history_user', models.ForeignKey(null=True, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-history_date', '-history_id'),
                'verbose_name': 'historical influence rating',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='HistoricalPopulation',
            fields=[
                ('id', models.IntegerField(db_index=True, verbose_name='ID', blank=True, auto_created=True)),
                ('name', models.CharField(max_length=200)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_type', models.CharField(max_length=1, choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')])),
                ('history_user', models.ForeignKey(null=True, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-history_date', '-history_id'),
                'verbose_name': 'historical population',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='HistoricalSession',
            fields=[
                ('id', models.IntegerField(db_index=True, verbose_name='ID', blank=True, auto_created=True)),
                ('name', models.CharField(max_length=200)),
                ('is_open', models.BooleanField(default=True)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_type', models.CharField(max_length=1, choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')])),
                ('history_user', models.ForeignKey(null=True, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-history_date', '-history_id'),
                'verbose_name': 'historical session',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='HistoricalTitle',
            fields=[
                ('id', models.IntegerField(db_index=True, verbose_name='ID', blank=True, auto_created=True)),
                ('name', models.CharField(max_length=200)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_type', models.CharField(max_length=1, choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')])),
                ('history_user', models.ForeignKey(null=True, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-history_date', '-history_id'),
                'verbose_name': 'historical title',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Influence',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='InfluenceRating',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('rating', models.PositiveIntegerField()),
                ('character', models.ForeignKey(to='players.Character', related_name='influences')),
                ('influence', models.ForeignKey(to='players.Influence')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Population',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=200)),
                ('is_open', models.BooleanField(default=True)),
                ('feeding_domains', models.ManyToManyField(to='players.Domain', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Title',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=200)),
                ('action_options', models.ManyToManyField(to='players.ActionOption', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='feeding',
            name='session',
            field=models.ForeignKey(to='players.Session', related_name='feedings'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='extraaction',
            name='session',
            field=models.ForeignKey(to='players.Session'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='domain',
            name='population',
            field=models.ForeignKey(to='players.Population'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='character',
            name='clan',
            field=models.ForeignKey(to='players.Clan'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='character',
            name='disciplines',
            field=models.ManyToManyField(to='players.Discipline', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='character',
            name='titles',
            field=models.ManyToManyField(to='players.Title', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='character',
            name='user',
            field=models.OneToOneField(null=True, to=settings.AUTH_USER_MODEL, blank=True, related_name='character'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='activedisciplines',
            name='character',
            field=models.ForeignKey(to='players.Character'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='activedisciplines',
            name='disciplines',
            field=models.ManyToManyField(to='players.Discipline', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='activedisciplines',
            name='session',
            field=models.ForeignKey(to='players.Session', related_name='active_disciplines'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='actionoption',
            name='action_types',
            field=models.ManyToManyField(to='players.ActionType'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='action',
            name='action_type',
            field=models.ForeignKey(to='players.ActionType'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='action',
            name='character',
            field=models.ForeignKey(to='players.Character'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='action',
            name='session',
            field=models.ForeignKey(to='players.Session', related_name='actions'),
            preserve_default=True,
        ),
    ]
