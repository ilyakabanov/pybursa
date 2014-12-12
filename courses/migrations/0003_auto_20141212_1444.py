# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_auto_20141210_1014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='city',
            field=models.CharField(max_length=100, verbose_name=b'\xd0\x93\xd0\xbe\xd1\x80\xd0\xbe\xd0\xb4'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='address',
            name='country',
            field=models.CharField(max_length=50, verbose_name=b'\xd0\xa1\xd1\x82\xd1\x80\xd0\xb0\xd0\xbd\xd0\xb0'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='address',
            name='district',
            field=models.CharField(max_length=100, verbose_name=b'\xd0\xa0\xd0\xb0\xd0\xb9\xd0\xbe\xd0\xbd'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='address',
            name='home',
            field=models.CharField(max_length=10, verbose_name=b'\xd0\x94\xd0\xbe\xd0\xbc'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='address',
            name='street',
            field=models.CharField(max_length=100, verbose_name=b'\xd0\xa3\xd0\xbb\xd0\xb8\xd1\x86\xd0\xb0'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='address',
            name='zcode',
            field=models.IntegerField(verbose_name=b'\xd0\x98\xd0\xbd\xd0\xb4\xd0\xb5\xd0\xba\xd1\x81'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='course',
            name='assistant',
            field=models.ForeignKey(related_name='assistant', verbose_name=b'\xd0\x90\xd1\x81\xd0\xb8\xd1\x81\xd1\x82\xd0\xb5\xd0\xbd\xd1\x82', to='coaches.Coach'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='course',
            name='coach',
            field=models.ForeignKey(verbose_name=b'\xd0\xa2\xd1\x80\xd0\xb5\xd0\xbd\xd0\xb5\xd1\x80', to='coaches.Coach'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='course',
            name='description',
            field=models.CharField(max_length=255, verbose_name=b'\xd0\x9e\xd0\xbf\xd0\xb8\xd1\x81\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='course',
            name='end_date',
            field=models.DateField(verbose_name=b'\xd0\x94\xd0\xb0\xd1\x82\xd0\xb0 \xd0\xbe\xd0\xba\xd0\xbe\xd0\xbd\xd1\x87\xd0\xb0\xd0\xbd\xd0\xb8\xd1\x8f'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='course',
            name='lang',
            field=models.CharField(default=b'python', max_length=8, verbose_name=b'\xd0\xaf\xd0\xb7\xd1\x8b\xd0\xba', choices=[(b'php', b'PHP 5.5'), (b'js', b'JavaScript'), (b'python', b'Python 2.7'), (b'rails', b'Ruby in Rails')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='course',
            name='name',
            field=models.CharField(max_length=255, verbose_name=b'\xd0\x9d\xd0\xb0\xd0\xb7\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='course',
            name='start_date',
            field=models.DateField(verbose_name=b'\xd0\x94\xd0\xb0\xd1\x82\xd0\xb0 \xd0\xbd\xd0\xb0\xd1\x87\xd0\xb0\xd0\xbb\xd0\xb0'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='course',
            name='venue',
            field=models.ForeignKey(verbose_name=b'\xd0\x9c\xd0\xb5\xd1\x81\xd1\x82\xd0\xbe', blank=True, to='courses.Address', null=True),
            preserve_default=True,
        ),
    ]
