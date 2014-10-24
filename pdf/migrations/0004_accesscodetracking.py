# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pdf', '0003_auto_20141015_0047'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccessCodeTracking',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_accessed', models.DateTimeField(auto_now=True, null=True)),
                ('access_code', models.ForeignKey(to='pdf.AccessCode')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
