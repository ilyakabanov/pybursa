# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('surname', models.CharField(max_length=255)),
                ('date_of_birth', models.DateField()),
                ('email', models.EmailField(max_length=75)),
                ('phone', models.CharField(max_length=15)),
                ('package', models.CharField(default=b'standart', max_length=8, choices=[(b'standart', b'\xd0\xa1\xd1\x82\xd0\xb0\xd0\xbd\xd0\xb4\xd0\xb0\xd1\x80\xd1\x82\xd0\xbd\xd1\x8b\xd0\xb9 \xd0\xbf\xd0\xb0\xd0\xba\xd0\xb5\xd1\x82'), (b'gold', b'\xd0\x97\xd0\xbe\xd0\xbb\xd0\xbe\xd1\x82\xd0\xbe\xd0\xb9 \xd0\xbf\xd0\xb0\xd0\xba\xd0\xb5\xd1\x82'), (b'vip', b'VIP \xd0\xbf\xd0\xb0\xd0\xba\xd0\xb5\xd1\x82')])),
                ('course', models.ForeignKey(to='courses.Course')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
