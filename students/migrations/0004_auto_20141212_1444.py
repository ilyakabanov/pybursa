# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0003_auto_20141210_1014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dossier',
            name='adress',
            field=models.ForeignKey(verbose_name=b'\xd0\x90\xd0\xb4\xd1\x80\xd0\xb5\xd1\x81', to='courses.Address'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='dossier',
            name='color',
            field=models.CharField(default=b'green', max_length=10, verbose_name=b'\xd0\x9b\xd1\x8e\xd0\xb1\xd0\xb8\xd0\xbc\xd1\x8b\xd0\xb9 \xd1\x86\xd0\xb2\xd0\xb5\xd1\x82', choices=[(b'ref', b'\xd0\x9a\xd1\x80\xd0\xb0\xd1\x81\xd0\xbd\xd1\x8b\xd0\xb9'), (b'orange', b'\xd0\x9e\xd1\x80\xd0\xb0\xd0\xbd\xd0\xb6\xd0\xb5\xd0\xb2\xd1\x8b\xd0\xb9'), (b'yellow', b'\xd0\x96\xd0\xb5\xd0\xbb\xd1\x82\xd1\x8b\xd0\xb9'), (b'green', b'\xd0\x97\xd0\xb5\xd0\xbb\xd0\xb5\xd0\xbd\xd1\x8b\xd0\xb9'), (b'lightblue', b'\xd0\x93\xd0\xbe\xd0\xbb\xd1\x83\xd0\xb1\xd0\xbe\xd0\xb9'), (b'blue', b'\xd0\xa1\xd0\xb8\xd0\xbd\xd0\xb8\xd0\xb9'), (b'purple', b'\xd0\xa4\xd0\xb8\xd0\xbe\xd0\xbb\xd0\xb5\xd1\x82\xd0\xbe\xd0\xb2\xd1\x8b\xd0\xb9')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='dossier',
            name='unloved_courses',
            field=models.ManyToManyField(to='courses.Course', null=True, verbose_name=b'\xd0\x9d\xd0\xb5\xd0\xbb\xd1\x8e\xd0\xb1\xd0\xb8\xd0\xbc\xd1\x8b\xd0\xb5 \xd0\xba\xd1\x83\xd1\x80\xd1\x81\xd1\x8b', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='student',
            name='courses',
            field=models.ManyToManyField(to='courses.Course', verbose_name=b'\xd0\x9a\xd1\x83\xd1\x80\xd1\x81\xd1\x8b'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='student',
            name='date_of_birth',
            field=models.DateField(verbose_name=b'\xd0\x94\xd0\xb0\xd1\x82\xd0\xb0 \xd1\x80\xd0\xbe\xd0\xb6\xd0\xb4\xd0\xb5\xd0\xbd\xd0\xb8\xd1\x8f'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='student',
            name='dossier',
            field=models.OneToOneField(null=True, blank=True, to='students.Dossier', verbose_name=b'\xd0\x94\xd0\xbe\xd1\x81\xd1\x8c\xd0\xb5'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='student',
            name='name',
            field=models.CharField(max_length=255, verbose_name=b'\xd0\x98\xd0\xbc\xd1\x8f'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='student',
            name='package',
            field=models.CharField(default=b'standart', max_length=8, verbose_name=b'\xd0\x9f\xd0\xb0\xd0\xba\xd0\xb5\xd1\x82', choices=[(b'standart', b'\xd0\xa1\xd1\x82\xd0\xb0\xd0\xbd\xd0\xb4\xd0\xb0\xd1\x80\xd1\x82\xd0\xbd\xd1\x8b\xd0\xb9 \xd0\xbf\xd0\xb0\xd0\xba\xd0\xb5\xd1\x82'), (b'gold', b'\xd0\x97\xd0\xbe\xd0\xbb\xd0\xbe\xd1\x82\xd0\xbe\xd0\xb9 \xd0\xbf\xd0\xb0\xd0\xba\xd0\xb5\xd1\x82'), (b'vip', b'VIP \xd0\xbf\xd0\xb0\xd0\xba\xd0\xb5\xd1\x82')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='student',
            name='phone',
            field=models.CharField(max_length=15, verbose_name=b'\xd0\xa2\xd0\xb5\xd0\xbb\xd0\xb5\xd1\x84\xd0\xbe\xd0\xbd'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='student',
            name='surname',
            field=models.CharField(max_length=255, verbose_name=b'\xd0\xa4\xd0\xb0\xd0\xbc\xd0\xb8\xd0\xbb\xd0\xb8\xd1\x8f'),
            preserve_default=True,
        ),
    ]
