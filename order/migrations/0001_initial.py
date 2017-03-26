# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='order_forms',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('seq', models.CharField(max_length=32, null=True, verbose_name='\u5de5\u5355\u7f16\u53f7', blank=True)),
                ('order_type', models.IntegerField(blank=True, null=True, verbose_name='\u5de5\u5355\u7c7b\u578b', choices=[(1, '\u76d1\u63a7\u534f\u52a9'), (2, 'DB\u534f\u52a9'), (3, '\u4e0a\u7ebf\u534f\u52a9'), (4, '\u6743\u9650\u7533\u8bf7'), (5, '\u4e3b\u673a\u7533\u8bf7'), (6, 'BLB\u7533\u8bf7'), (4, '\u5bbd\u5e26\u7533\u8bf7'), (5, '\u5176\u4ed6\u534f\u52a9')])),
                ('order_title', models.CharField(max_length=256, null=True, verbose_name='\u5de5\u5355\u540d\u79f0', blank=True)),
                ('order_text', models.TextField(default='', null=True, verbose_name='\u5de5\u5355\u5185\u5bb9', blank=True)),
                ('date_added', models.DateTimeField(auto_now=True, null=True)),
                ('end_time', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'verbose_name': '\u5de5\u5355',
                'verbose_name_plural': '\u5de5\u5355',
            },
        ),
        migrations.CreateModel(
            name='order_group',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('g_name', models.CharField(max_length=100, null=True, verbose_name='\u7ec4\u540d\u79f0', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='order_user',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('u_name', models.CharField(max_length=100, null=True, verbose_name='\u8d26\u53f7', blank=True)),
                ('u_password', models.CharField(max_length=100, null=True, verbose_name='\u5bc6\u7801', blank=True)),
                ('r_name', models.CharField(max_length=100, null=True, verbose_name='\u771f\u662f\u59d3\u540d', blank=True)),
                ('u_mail', models.EmailField(max_length=254)),
                ('u_gid', models.ForeignKey(verbose_name='\u7ec4ID', blank=True, to='order.order_group', null=True)),
            ],
        ),
        migrations.AddField(
            model_name='order_forms',
            name='faqi_user',
            field=models.ForeignKey(verbose_name='\u53d1\u8d77\u7528\u6237', blank=True, to='order.order_user'),
        ),
    ]
