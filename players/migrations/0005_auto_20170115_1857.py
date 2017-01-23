# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2017-01-15 18:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0004_auto_20170115_1802'),
    ]

    operations = [
        migrations.CreateModel(
            name='InfluencePriority',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('cost', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ResourcePriority',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('cost', models.PositiveIntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='investigatecharacterinfluence',
            name='priority1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='priority1', to='players.InfluencePriority'),
        ),
        migrations.AlterField(
            model_name='investigatecharacterinfluence',
            name='priority2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='priority2', to='players.InfluencePriority'),
        ),
        migrations.AlterField(
            model_name='investigatecharacterinfluence',
            name='priority3',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='priority3', to='players.InfluencePriority'),
        ),
        migrations.AlterField(
            model_name='investigatecharacterinfluence',
            name='priority4',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='priority4', to='players.InfluencePriority'),
        ),
        migrations.AlterField(
            model_name='investigatecharacterinfluence',
            name='priority5',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='priority5', to='players.InfluencePriority'),
        ),
        migrations.AlterField(
            model_name='investigatecharacterinfluence',
            name='priority6',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='priority6', to='players.InfluencePriority'),
        ),
        migrations.AlterField(
            model_name='investigatecharacterinfluence',
            name='priority7',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='priority7', to='players.InfluencePriority'),
        ),
        migrations.AlterField(
            model_name='investigatecharacterinfluence',
            name='priority8',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='priority8', to='players.InfluencePriority'),
        ),
        migrations.AlterField(
            model_name='investigatecharacterresources',
            name='priority1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='priority1', to='players.ResourcePriority'),
        ),
        migrations.AlterField(
            model_name='investigatecharacterresources',
            name='priority2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='priority2', to='players.ResourcePriority'),
        ),
        migrations.AlterField(
            model_name='investigatecharacterresources',
            name='priority3',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='priority3', to='players.ResourcePriority'),
        ),
        migrations.AlterField(
            model_name='investigatecharacterresources',
            name='priority4',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='priority4', to='players.ResourcePriority'),
        ),
        migrations.AlterField(
            model_name='investigatecharacterresources',
            name='priority5',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='priority5', to='players.ResourcePriority'),
        ),
        migrations.AlterField(
            model_name='investigatecharacterresources',
            name='priority6',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='priority6', to='players.ResourcePriority'),
        ),
        migrations.AlterField(
            model_name='investigatecharacterresources',
            name='priority7',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='priority7', to='players.ResourcePriority'),
        ),
        migrations.AlterField(
            model_name='investigatecharacterresources',
            name='priority8',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='priority8', to='players.ResourcePriority'),
        ),
    ]
