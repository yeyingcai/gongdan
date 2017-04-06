# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('asset', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='j_docker',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=32, null=True, verbose_name='\u4e3b\u673a\u540d', blank=True)),
                ('ssh_ip', models.TextField(default='', null=True, verbose_name='ssh\u5730\u5740', blank=True)),
                ('ssh_port', models.CharField(max_length=12, null=True, verbose_name='ssh\u7aef\u53e3', blank=True)),
                ('service', models.CharField(max_length=64, null=True, verbose_name='\u670d\u52a1', blank=True)),
                ('port', models.CharField(max_length=12, null=True, verbose_name='\u670d\u52a1\u7aef\u53e3', blank=True)),
                ('img_name', models.CharField(max_length=24, null=True, verbose_name='\u955c\u50cf\u540d\u79f0', blank=True)),
                ('file_path', models.TextField(null=True, verbose_name='DOCKERFILE', blank=True)),
                ('comment', models.CharField(max_length=128, null=True, verbose_name='\u5907\u6ce8', blank=True)),
                ('p_host', models.ForeignKey(verbose_name='\u5bbf\u4e3b\u673a', blank=True, to='asset.j_Asset', null=True)),
            ],
            options={
                'verbose_name': 'docker',
                'verbose_name_plural': 'docker',
            },
        ),
    ]
