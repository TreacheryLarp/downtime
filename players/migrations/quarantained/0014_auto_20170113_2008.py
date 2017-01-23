# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2017-01-13 20:08
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('players', '0013_auto_20170113_1909'),
    ]

    operations = [
        migrations.CreateModel(
            name='BloodBond',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('degree', models.PositiveIntegerField(choices=[(1, 1), (2, 2), (3, 3)], default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('level', models.PositiveIntegerField(choices=[(1, 1), (2, 2), (3, 3)], default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Ghoul',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('level', models.PositiveIntegerField(choices=[(1, 1), (2, 2), (3, 3)], default=1)),
                ('disciplines', models.ManyToManyField(blank=True, to='players.DisciplineRating')),
                ('hook', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='players.Hook')),
                ('specializations', models.ManyToManyField(blank=True, to='players.Specialization')),
            ],
        ),
        migrations.CreateModel(
            name='HistoricalRelationship',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('description', models.TextField()),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
            ],
            options={
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
                'verbose_name': 'historical relationship',
            },
        ),
        migrations.CreateModel(
            name='Relationship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
            ],
        ),
        migrations.RenameField(
            model_name='character',
            old_name='goal3',
            new_name='hiddenGoal',
        ),
        migrations.RenameField(
            model_name='character',
            old_name='goal1',
            new_name='openGoal1',
        ),
        migrations.RenameField(
            model_name='character',
            old_name='goal2',
            new_name='openGoal2',
        ),
        migrations.RenameField(
            model_name='historicalcharacter',
            old_name='goal3',
            new_name='hiddenGoal',
        ),
        migrations.RenameField(
            model_name='historicalcharacter',
            old_name='goal1',
            new_name='openGoal1',
        ),
        migrations.RenameField(
            model_name='historicalcharacter',
            old_name='goal2',
            new_name='openGoal2',
        ),
        migrations.AddField(
            model_name='character',
            name='concept',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='character',
            name='generation',
            field=models.PositiveIntegerField(default=13),
        ),
        migrations.AddField(
            model_name='character',
            name='haven',
            field=models.PositiveIntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3)], default=0),
        ),
        migrations.AddField(
            model_name='character',
            name='herd',
            field=models.PositiveIntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3)], default=0),
        ),
        migrations.AddField(
            model_name='clan',
            name='theme',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='historicalcharacter',
            name='concept',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='historicalcharacter',
            name='generation',
            field=models.PositiveIntegerField(default=13),
        ),
        migrations.AddField(
            model_name='historicalcharacter',
            name='haven',
            field=models.PositiveIntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3)], default=0),
        ),
        migrations.AddField(
            model_name='historicalcharacter',
            name='herd',
            field=models.PositiveIntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3)], default=0),
        ),
        migrations.AddField(
            model_name='historicalclan',
            name='theme',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='historicalpoliticalfraction',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='politicalfraction',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='character',
            name='relationships',
            field=models.ManyToManyField(blank=True, to='players.Relationship'),
        ),
        migrations.AddField(
            model_name='relationship',
            name='char',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='players.Character'),
        ),
        migrations.AddField(
            model_name='historicalrelationship',
            name='char',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='players.Character'),
        ),
        migrations.AddField(
            model_name='historicalrelationship',
            name='history_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='bloodbond',
            name='master',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='players.Character'),
        ),
        migrations.AddField(
            model_name='character',
            name='bloodBond',
            field=models.ManyToManyField(blank=True, to='players.BloodBond'),
        ),
        migrations.AddField(
            model_name='character',
            name='equipment',
            field=models.ManyToManyField(blank=True, to='players.Equipment'),
        ),
        migrations.AddField(
            model_name='character',
            name='ghouls',
            field=models.ManyToManyField(blank=True, to='players.Ghoul'),
        ),
    ]
