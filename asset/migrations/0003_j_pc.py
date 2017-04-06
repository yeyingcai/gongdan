# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('asset', '0002_j_docker'),
    ]

    operations = [
        migrations.CreateModel(
            name='j_pc',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('brand', models.CharField(max_length=32, null=True, verbose_name='\u54c1\u724c', blank=True)),
                ('pc_type', models.IntegerField(blank=True, null=True, verbose_name='\u7c7b\u578b', choices=[(1, '\u53f0\u5f0f\u673a'), (2, '\u7b14\u8bb0\u672c')])),
                ('cpu', models.CharField(max_length=64, null=True, verbose_name='CPU', blank=True)),
                ('mem', models.CharField(max_length=12, null=True, verbose_name='\u5185\u5b58', blank=True)),
                ('disk', models.CharField(max_length=12, null=True, verbose_name='\u786c\u76d8', blank=True)),
                ('sn', models.CharField(max_length=64, null=True, verbose_name='\u8d44\u4ea7\u7f16\u7801', blank=True)),
                ('owner', models.CharField(max_length=32, null=True, verbose_name='\u4f7f\u7528\u4eba', blank=True)),
                ('comment', models.CharField(max_length=128, null=True, verbose_name='\u5907\u6ce8', blank=True)),
            ],
            options={
                'verbose_name': 'PC\u4e3b\u673a',
                'verbose_name_plural': 'PC\u4e3b\u673a',
            },
        ),
    ]
