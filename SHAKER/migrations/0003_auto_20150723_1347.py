# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SHAKER', '0002_auto_20150722_2130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ibdm',
            name='iZ',
            field=models.CharField(default=False, max_length=200, null=True, editable=False, blank=True),
        ),
        migrations.AlterField(
            model_name='ville_bardumonde',
            name='iZ',
            field=models.CharField(default=False, max_length=200, null=True, editable=False, blank=True),
        ),
    ]
