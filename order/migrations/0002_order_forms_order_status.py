# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order_forms',
            name='order_status',
            field=models.CharField(default='0', max_length=3, verbose_name='\u5de5\u5355\u72b6\u6001'),
        ),
    ]
