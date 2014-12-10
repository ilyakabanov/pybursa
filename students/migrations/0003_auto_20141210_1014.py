# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_auto_20141210_1014'),
        ('students', '0002_auto_20141209_2007'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dossier',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('color', models.CharField(default=b'green', max_length=10, choices=[(b'ref', b'\xd0\x9a\xd1\x80\xd0\xb0\xd1\x81\xd0\xbd\xd1\x8b\xd0\xb9'), (b'orange', b'\xd0\x9e\xd1\x80\xd0\xb0\xd0\xbd\xd0\xb6\xd0\xb5\xd0\xb2\xd1\x8b\xd0\xb9'), (b'yellow', b'\xd0\x96\xd0\xb5\xd0\xbb\xd1\x82\xd1\x8b\xd0\xb9'), (b'green', b'\xd0\x97\xd0\xb5\xd0\xbb\xd0\xb5\xd0\xbd\xd1\x8b\xd0\xb9'), (b'lightblue', b'\xd0\x93\xd0\xbe\xd0\xbb\xd1\x83\xd0\xb1\xd0\xbe\xd0\xb9'), (b'blue', b'\xd0\xa1\xd0\xb8\xd0\xbd\xd0\xb8\xd0\xb9'), (b'purple', b'\xd0\xa4\xd0\xb8\xd0\xbe\xd0\xbb\xd0\xb5\xd1\x82\xd0\xbe\xd0\xb2\xd1\x8b\xd0\xb9')])),
                ('adress', models.ForeignKey(to='courses.Address')),
                ('unloved_courses', models.ManyToManyField(to='courses.Course', null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='student',
            name='dossier',
            field=models.OneToOneField(null=True, blank=True, to='students.Dossier'),
            preserve_default=True,
        ),
    ]
