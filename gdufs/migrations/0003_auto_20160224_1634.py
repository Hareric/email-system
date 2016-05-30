# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gdufs', '0002_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='email',
            name='time',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='email',
            name='title',
            field=models.TextField(),
        ),
    ]
