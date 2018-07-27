# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-07-27 16:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0042_auto_20180724_1816'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReportingPeriodStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='Title')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Text')),
                ('is_done', models.BooleanField(verbose_name='Status represents reporting period is closed')),
            ],
            options={
                'verbose_name': 'Reporting Period Status',
                'verbose_name_plural': 'Reporting Period Status',
            },
        ),
    ]
