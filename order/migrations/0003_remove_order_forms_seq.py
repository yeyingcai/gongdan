# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_order_forms_order_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order_forms',
            name='seq',
        ),
    ]
