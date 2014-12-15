# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0003_auto_20141208_1837'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='student',
            name='email',
            field=models.EmailField(help_text=b'Not unical email', max_length=75),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='student',
            name='name',
            field=models.CharField(max_length=255, verbose_name=b'NA-ME'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='student',
            name='package',
            field=models.CharField(db_index=True, max_length=15, choices=[(b'standart', b'Standart'), (b'gold', b'Gold'), (b'vip', b'VIP')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='student',
            name='surname',
            field=models.CharField(default=b'asd', max_length=255, blank=True),
            preserve_default=True,
        ),
    ]
