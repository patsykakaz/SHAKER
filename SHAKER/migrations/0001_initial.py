# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_auto_20150527_1555'),
    ]

    operations = [
        migrations.CreateModel(
            name='BarDuMonde',
            fields=[
                ('page_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='pages.Page')),
                ('date_derniere_visite', models.DateField(null=True, blank=True)),
                ('illustration', models.ImageField(upload_to='/home/patsykakaz/SHAKERenv/SHAKER/static/media', verbose_name=b'Illustration du Bar; Taille recommand\xc3\xa9e: 800x450; Poids maximal recommand\xc3\xa9: 100 Ko')),
                ('site_web', models.URLField(help_text=b'entrez une adresse URL valide', null=True, verbose_name=b'Site internet', blank=True)),
                ('facebook', models.URLField(null=True, blank=True)),
                ('twitter', models.URLField(null=True, blank=True)),
                ('adresse', models.CharField(max_length=200, null=True)),
                ('barman_vedette', models.TextField(help_text=b'Description du Barman', null=True, verbose_name=b'Barman Vedette', blank=True)),
                ('cocktail', models.TextField(help_text=b'Description du cocktail vedette', null=True, blank=True)),
                ('decoration', models.TextField(help_text=b'Description de la d\xc3\xa9coration', null=True, verbose_name=b'd\xc3\xa9coration', blank=True)),
            ],
            options={
                'ordering': ('_order',),
                'verbose_name': 'Bar Du Monde',
            },
            bases=('pages.page',),
        ),
        migrations.CreateModel(
            name='IBDM',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('illustration', django_resized.forms.ResizedImageField(upload_to='/home/patsykakaz/SHAKERenv/SHAKER/static/media/bar_du_monde')),
                ('iZ', models.CharField(default=False, max_length=500, null=True, editable=False, blank=True)),
                ('legende', models.CharField(help_text=b'400 caract\xc3\xa8res max', max_length=400, null=True, verbose_name=b'l\xc3\xa9gende', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Publicite',
            fields=[
                ('page_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='pages.Page')),
                ('lien', models.CharField(max_length=255, null=True, blank=True)),
                ('media', models.ImageField(null=True, upload_to='/home/patsykakaz/SHAKERenv/SHAKER/static/media/publicite')),
                ('formatPub', models.CharField(max_length=250, null=True, choices=[(b'HABILLAGE', b'HABILLAGE'), (b'SQUARE', b'SQUARE'), (b'COLONNE', b'COLONNE')])),
            ],
            options={
                'ordering': ('_order',),
            },
            bases=('pages.page',),
        ),
        migrations.CreateModel(
            name='Ville_BarDuMonde',
            fields=[
                ('page_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='pages.Page')),
                ('illustration', models.ImageField(upload_to='/home/patsykakaz/SHAKERenv/SHAKER/static/media', verbose_name=b'Illustration de la ville; Taille recommand\xc3\xa9e: 1000x400; Poids maximal recommand\xc3\xa9: 150 Ko')),
            ],
            options={
                'ordering': ('_order',),
                'verbose_name': 'Ville (Bars du Monde)',
            },
            bases=('pages.page',),
        ),
        migrations.CreateModel(
            name='IBDM_BarmanVedette',
            fields=[
                ('ibdm_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='SHAKER.IBDM')),
            ],
            bases=('SHAKER.ibdm',),
        ),
        migrations.CreateModel(
            name='IBDM_Cocktail',
            fields=[
                ('ibdm_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='SHAKER.IBDM')),
            ],
            bases=('SHAKER.ibdm',),
        ),
        migrations.CreateModel(
            name='IBDM_Decoration',
            fields=[
                ('ibdm_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='SHAKER.IBDM')),
            ],
            bases=('SHAKER.ibdm',),
        ),
        migrations.AddField(
            model_name='ibdm',
            name='bar',
            field=models.ForeignKey(to='SHAKER.BarDuMonde'),
        ),
        migrations.AddField(
            model_name='bardumonde',
            name='ville',
            field=models.ForeignKey(verbose_name=b'Ville du bar', to='SHAKER.Ville_BarDuMonde'),
        ),
    ]
