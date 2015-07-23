# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('SHAKER', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ville_bardumonde',
            name='iZ',
            field=models.CharField(default=False, max_length=500, null=True, editable=False, blank=True),
        ),
        migrations.AlterField(
            model_name='ville_bardumonde',
            name='illustration',
            field=django_resized.forms.ResizedImageField(upload_to='/home/patsykakaz/SHAKERenv/SHAKER/static/media/villes_BDM'),
        ),
    ]
