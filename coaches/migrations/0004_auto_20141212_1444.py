# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('coaches', '0003_coach_dossier'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coach',
            name='date_of_birth',
            field=models.DateField(verbose_name=b'\xd0\x94\xd0\xb0\xd1\x82\xd0\xb0 \xd1\x80\xd0\xbe\xd0\xb6\xd0\xb4\xd0\xb5\xd0\xbd\xd0\xb8\xd1\x8f'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='coach',
            name='dossier',
            field=models.OneToOneField(null=True, blank=True, to='students.Dossier', verbose_name=b'\xd0\x94\xd0\xbe\xd1\x81\xd1\x8c\xd0\xb5'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='coach',
            name='name',
            field=models.CharField(max_length=255, verbose_name=b'\xd0\x98\xd0\xbc\xd1\x8f'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='coach',
            name='phone',
            field=models.CharField(max_length=15, verbose_name=b'\xd0\xa2\xd0\xb5\xd0\xbb\xd0\xb5\xd1\x84\xd0\xbe\xd0\xbd'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='coach',
            name='role',
            field=models.CharField(default=b'coach', max_length=5, verbose_name=b'\xd0\xa0\xd0\xbe\xd0\xbb\xd1\x8c', choices=[(b'coach', b'\xd0\xa2\xd1\x80\xd0\xb5\xd0\xbd\xd0\xb5\xd1\x80'), (b'asist', b'\xd0\x90\xd1\x81\xd0\xb8\xd1\x81\xd1\x82\xd0\xb5\xd0\xbd\xd1\x82')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='coach',
            name='surname',
            field=models.CharField(max_length=255, verbose_name=b'\xd0\xa4\xd0\xb0\xd0\xbc\xd0\xb8\xd0\xbb\xd0\xb8\xd1\x8f'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='coach',
            name='user',
            field=models.ForeignKey(verbose_name=b'\xd0\xae\xd0\xb7\xd0\xb5\xd1\x80', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
