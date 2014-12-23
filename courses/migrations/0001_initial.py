# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coaches', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('lang', models.CharField(default=b'python', max_length=8, choices=[(b'php', b'PHP 5.5'), (b'js', b'JavaScript'), (b'python', b'Python 2.7'), (b'rails', b'Ruby in Rails')])),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('assistant', models.ForeignKey(related_name='assistant', to='coaches.Coach')),
                ('coach', models.ForeignKey(to='coaches.Coach')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
