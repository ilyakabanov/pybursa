# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0007_auto_20141208_2003'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='slug',
            field=models.SlugField(default='a'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='student',
            name='surname',
            field=models.CharField(max_length=255, blank=True),
            preserve_default=True,
        ),
    ]
