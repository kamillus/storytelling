# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pdf', '0004_accesscodetracking'),
    ]

    operations = [
        migrations.AddField(
            model_name='accesscodetracking',
            name='action',
            field=models.CharField(max_length=30, null=True),
            preserve_default=True,
        ),
    ]
