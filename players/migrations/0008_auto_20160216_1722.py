# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-16 17:22
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('players', '0007_auto_20160204_1133'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='historicalaction',
            options={'get_latest_by': 'history_date',
                     'ordering': ('-history_date', '-history_id'),
                     'verbose_name': 'historical action'}, ),
        migrations.AlterModelOptions(
            name='historicalactionoption',
            options={'get_latest_by': 'history_date',
                     'ordering': ('-history_date', '-history_id'),
                     'verbose_name': 'historical action option'}, ),
        migrations.AlterModelOptions(
            name='historicalactiontype',
            options={'get_latest_by': 'history_date',
                     'ordering': ('-history_date', '-history_id'),
                     'verbose_name': 'historical action type'}, ),
        migrations.AlterModelOptions(
            name='historicalactivedisciplines',
            options={'get_latest_by': 'history_date',
                     'ordering': ('-history_date', '-history_id'),
                     'verbose_name': 'historical active disciplines'}, ),
        migrations.AlterModelOptions(
            name='historicalage',
            options={'get_latest_by': 'history_date',
                     'ordering': ('-history_date', '-history_id'),
                     'verbose_name': 'historical age'}, ),
        migrations.AlterModelOptions(
            name='historicalcharacter',
            options={'get_latest_by': 'history_date',
                     'ordering': ('-history_date', '-history_id'),
                     'verbose_name': 'historical character'}, ),
        migrations.AlterModelOptions(
            name='historicalclan',
            options={'get_latest_by': 'history_date',
                     'ordering': ('-history_date', '-history_id'),
                     'verbose_name': 'historical clan'}, ),
        migrations.AlterModelOptions(
            name='historicaldiscipline',
            options={'get_latest_by': 'history_date',
                     'ordering': ('-history_date', '-history_id'),
                     'verbose_name': 'historical discipline'}, ),
        migrations.AlterModelOptions(
            name='historicaldomain',
            options={'get_latest_by': 'history_date',
                     'ordering': ('-history_date', '-history_id'),
                     'verbose_name': 'historical domain'}, ),
        migrations.AlterModelOptions(
            name='historicalextraaction',
            options={'get_latest_by': 'history_date',
                     'ordering': ('-history_date', '-history_id'),
                     'verbose_name': 'historical extra action'}, ),
        migrations.AlterModelOptions(
            name='historicalfeeding',
            options={'get_latest_by': 'history_date',
                     'ordering': ('-history_date', '-history_id'),
                     'verbose_name': 'historical feeding'}, ),
        migrations.AlterModelOptions(
            name='historicalinfluence',
            options={'get_latest_by': 'history_date',
                     'ordering': ('-history_date', '-history_id'),
                     'verbose_name': 'historical influence'}, ),
        migrations.AlterModelOptions(
            name='historicalinfluencerating',
            options={'get_latest_by': 'history_date',
                     'ordering': ('-history_date', '-history_id'),
                     'verbose_name': 'historical influence rating'}, ),
        migrations.AlterModelOptions(
            name='historicalpopulation',
            options={'get_latest_by': 'history_date',
                     'ordering': ('-history_date', '-history_id'),
                     'verbose_name': 'historical population'}, ),
        migrations.AlterModelOptions(
            name='historicalsession',
            options={'get_latest_by': 'history_date',
                     'ordering': ('-history_date', '-history_id'),
                     'verbose_name': 'historical session'}, ),
        migrations.AlterModelOptions(
            name='historicaltitle',
            options={'get_latest_by': 'history_date',
                     'ordering': ('-history_date', '-history_id'),
                     'verbose_name': 'historical title'}, ),
        migrations.RemoveField(model_name='historicalaction',
                               name='action_type_id', ),
        migrations.RemoveField(model_name='historicalaction',
                               name='character_id', ),
        migrations.RemoveField(model_name='historicalaction',
                               name='session_id', ),
        migrations.RemoveField(model_name='historicalactivedisciplines',
                               name='character_id', ),
        migrations.RemoveField(model_name='historicalactivedisciplines',
                               name='session_id', ),
        migrations.RemoveField(model_name='historicalcharacter',
                               name='age_id', ),
        migrations.RemoveField(model_name='historicalcharacter',
                               name='clan_id', ),
        migrations.RemoveField(model_name='historicalcharacter',
                               name='user_id', ),
        migrations.RemoveField(model_name='historicalextraaction',
                               name='character_id', ),
        migrations.RemoveField(model_name='historicalextraaction',
                               name='session_id', ),
        migrations.RemoveField(model_name='historicalfeeding',
                               name='character_id', ),
        migrations.RemoveField(model_name='historicalfeeding',
                               name='discipline_id', ),
        migrations.RemoveField(model_name='historicalfeeding',
                               name='domain_id', ),
        migrations.RemoveField(model_name='historicalfeeding',
                               name='session_id', ),
        migrations.RemoveField(model_name='historicalinfluencerating',
                               name='character_id', ),
        migrations.RemoveField(model_name='historicalinfluencerating',
                               name='influence_id', ),
        migrations.AddField(model_name='historicalaction',
                            name='action_type',
                            field=models.ForeignKey(
                                blank=True,
                                db_constraint=False,
                                null=True,
                                on_delete=django.db.models.deletion.DO_NOTHING,
                                related_name='+',
                                to='players.ActionType'), ),
        migrations.AddField(model_name='historicalaction',
                            name='character',
                            field=models.ForeignKey(
                                blank=True,
                                db_constraint=False,
                                null=True,
                                on_delete=django.db.models.deletion.DO_NOTHING,
                                related_name='+',
                                to='players.Character'), ),
        migrations.AddField(model_name='historicalaction',
                            name='session',
                            field=models.ForeignKey(
                                blank=True,
                                db_constraint=False,
                                null=True,
                                on_delete=django.db.models.deletion.DO_NOTHING,
                                related_name='+',
                                to='players.Session'), ),
        migrations.AddField(model_name='historicalactivedisciplines',
                            name='character',
                            field=models.ForeignKey(
                                blank=True,
                                db_constraint=False,
                                null=True,
                                on_delete=django.db.models.deletion.DO_NOTHING,
                                related_name='+',
                                to='players.Character'), ),
        migrations.AddField(model_name='historicalactivedisciplines',
                            name='session',
                            field=models.ForeignKey(
                                blank=True,
                                db_constraint=False,
                                null=True,
                                on_delete=django.db.models.deletion.DO_NOTHING,
                                related_name='+',
                                to='players.Session'), ),
        migrations.AddField(model_name='historicalcharacter',
                            name='age',
                            field=models.ForeignKey(
                                blank=True,
                                db_constraint=False,
                                null=True,
                                on_delete=django.db.models.deletion.DO_NOTHING,
                                related_name='+',
                                to='players.Age'), ),
        migrations.AddField(model_name='historicalcharacter',
                            name='clan',
                            field=models.ForeignKey(
                                blank=True,
                                db_constraint=False,
                                null=True,
                                on_delete=django.db.models.deletion.DO_NOTHING,
                                related_name='+',
                                to='players.Clan'), ),
        migrations.AddField(model_name='historicalcharacter',
                            name='user',
                            field=models.ForeignKey(
                                blank=True,
                                db_constraint=False,
                                null=True,
                                on_delete=django.db.models.deletion.DO_NOTHING,
                                related_name='+',
                                to=settings.AUTH_USER_MODEL), ),
        migrations.AddField(model_name='historicalextraaction',
                            name='character',
                            field=models.ForeignKey(
                                blank=True,
                                db_constraint=False,
                                null=True,
                                on_delete=django.db.models.deletion.DO_NOTHING,
                                related_name='+',
                                to='players.Character'), ),
        migrations.AddField(model_name='historicalextraaction',
                            name='session',
                            field=models.ForeignKey(
                                blank=True,
                                db_constraint=False,
                                null=True,
                                on_delete=django.db.models.deletion.DO_NOTHING,
                                related_name='+',
                                to='players.Session'), ),
        migrations.AddField(model_name='historicalfeeding',
                            name='character',
                            field=models.ForeignKey(
                                blank=True,
                                db_constraint=False,
                                null=True,
                                on_delete=django.db.models.deletion.DO_NOTHING,
                                related_name='+',
                                to='players.Character'), ),
        migrations.AddField(model_name='historicalfeeding',
                            name='discipline',
                            field=models.ForeignKey(
                                blank=True,
                                db_constraint=False,
                                null=True,
                                on_delete=django.db.models.deletion.DO_NOTHING,
                                related_name='+',
                                to='players.Discipline'), ),
        migrations.AddField(model_name='historicalfeeding',
                            name='domain',
                            field=models.ForeignKey(
                                blank=True,
                                db_constraint=False,
                                null=True,
                                on_delete=django.db.models.deletion.DO_NOTHING,
                                related_name='+',
                                to='players.Domain'), ),
        migrations.AddField(model_name='historicalfeeding',
                            name='session',
                            field=models.ForeignKey(
                                blank=True,
                                db_constraint=False,
                                null=True,
                                on_delete=django.db.models.deletion.DO_NOTHING,
                                related_name='+',
                                to='players.Session'), ),
        migrations.AddField(model_name='historicalinfluencerating',
                            name='character',
                            field=models.ForeignKey(
                                blank=True,
                                db_constraint=False,
                                null=True,
                                on_delete=django.db.models.deletion.DO_NOTHING,
                                related_name='+',
                                to='players.Character'), ),
        migrations.AddField(model_name='historicalinfluencerating',
                            name='influence',
                            field=models.ForeignKey(
                                blank=True,
                                db_constraint=False,
                                null=True,
                                on_delete=django.db.models.deletion.DO_NOTHING,
                                related_name='+',
                                to='players.Influence'), ),
        migrations.AlterField(model_name='historicalaction',
                              name='history_user',
                              field=models.ForeignKey(
                                  null=True,
                                  on_delete=django.db.models.deletion.SET_NULL,
                                  related_name='+',
                                  to=settings.AUTH_USER_MODEL), ),
        migrations.AlterField(model_name='historicalactionoption',
                              name='history_user',
                              field=models.ForeignKey(
                                  null=True,
                                  on_delete=django.db.models.deletion.SET_NULL,
                                  related_name='+',
                                  to=settings.AUTH_USER_MODEL), ),
        migrations.AlterField(model_name='historicalactiontype',
                              name='history_user',
                              field=models.ForeignKey(
                                  null=True,
                                  on_delete=django.db.models.deletion.SET_NULL,
                                  related_name='+',
                                  to=settings.AUTH_USER_MODEL), ),
        migrations.AlterField(model_name='historicalactivedisciplines',
                              name='history_user',
                              field=models.ForeignKey(
                                  null=True,
                                  on_delete=django.db.models.deletion.SET_NULL,
                                  related_name='+',
                                  to=settings.AUTH_USER_MODEL), ),
        migrations.AlterField(model_name='historicalage',
                              name='history_user',
                              field=models.ForeignKey(
                                  null=True,
                                  on_delete=django.db.models.deletion.SET_NULL,
                                  related_name='+',
                                  to=settings.AUTH_USER_MODEL), ),
        migrations.AlterField(model_name='historicalcharacter',
                              name='history_user',
                              field=models.ForeignKey(
                                  null=True,
                                  on_delete=django.db.models.deletion.SET_NULL,
                                  related_name='+',
                                  to=settings.AUTH_USER_MODEL), ),
        migrations.AlterField(model_name='historicalclan',
                              name='history_user',
                              field=models.ForeignKey(
                                  null=True,
                                  on_delete=django.db.models.deletion.SET_NULL,
                                  related_name='+',
                                  to=settings.AUTH_USER_MODEL), ),
        migrations.AlterField(model_name='historicaldiscipline',
                              name='history_user',
                              field=models.ForeignKey(
                                  null=True,
                                  on_delete=django.db.models.deletion.SET_NULL,
                                  related_name='+',
                                  to=settings.AUTH_USER_MODEL), ),
        migrations.AlterField(model_name='historicaldomain',
                              name='history_user',
                              field=models.ForeignKey(
                                  null=True,
                                  on_delete=django.db.models.deletion.SET_NULL,
                                  related_name='+',
                                  to=settings.AUTH_USER_MODEL), ),
        migrations.AlterField(model_name='historicalextraaction',
                              name='history_user',
                              field=models.ForeignKey(
                                  null=True,
                                  on_delete=django.db.models.deletion.SET_NULL,
                                  related_name='+',
                                  to=settings.AUTH_USER_MODEL), ),
        migrations.AlterField(model_name='historicalfeeding',
                              name='history_user',
                              field=models.ForeignKey(
                                  null=True,
                                  on_delete=django.db.models.deletion.SET_NULL,
                                  related_name='+',
                                  to=settings.AUTH_USER_MODEL), ),
        migrations.AlterField(model_name='historicalinfluence',
                              name='history_user',
                              field=models.ForeignKey(
                                  null=True,
                                  on_delete=django.db.models.deletion.SET_NULL,
                                  related_name='+',
                                  to=settings.AUTH_USER_MODEL), ),
        migrations.AlterField(model_name='historicalinfluencerating',
                              name='history_user',
                              field=models.ForeignKey(
                                  null=True,
                                  on_delete=django.db.models.deletion.SET_NULL,
                                  related_name='+',
                                  to=settings.AUTH_USER_MODEL), ),
        migrations.AlterField(model_name='historicalpopulation',
                              name='history_user',
                              field=models.ForeignKey(
                                  null=True,
                                  on_delete=django.db.models.deletion.SET_NULL,
                                  related_name='+',
                                  to=settings.AUTH_USER_MODEL), ),
        migrations.AlterField(model_name='historicalsession',
                              name='history_user',
                              field=models.ForeignKey(
                                  null=True,
                                  on_delete=django.db.models.deletion.SET_NULL,
                                  related_name='+',
                                  to=settings.AUTH_USER_MODEL), ),
        migrations.AlterField(model_name='historicaltitle',
                              name='history_user',
                              field=models.ForeignKey(
                                  null=True,
                                  on_delete=django.db.models.deletion.SET_NULL,
                                  related_name='+',
                                  to=settings.AUTH_USER_MODEL), ),
    ]
