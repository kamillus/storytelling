# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pdf', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='accesscode',
            name='date_of_release',
            field=models.DateTimeField(null=True),
            preserve_default=True,
        ),
    ]
