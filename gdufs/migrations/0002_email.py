# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gdufs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mid', models.CharField(default=b'null', max_length=30)),
                ('content', models.TextField()),
                ('time', models.TimeField()),
                ('from_email', models.EmailField(max_length=254)),
                ('from_name', models.CharField(max_length=20)),
                ('title', models.CharField(max_length=50)),
                ('to_ID_number', models.CharField(max_length=11)),
                ('to_name', models.CharField(max_length=20)),
            ],
        ),
    ]
