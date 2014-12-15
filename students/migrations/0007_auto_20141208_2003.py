# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0006_student_courses'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='kurator_group',
            field=models.ForeignKey(related_name='kurators', default=1, to='students.Group'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='student',
            name='group',
            field=models.ForeignKey(related_name='students', to='students.Group'),
            preserve_default=True,
        ),
    ]
