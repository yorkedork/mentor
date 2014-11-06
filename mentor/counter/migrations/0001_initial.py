# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Counter',
            fields=[
                ('url_id', models.AutoField(primary_key=True, serialize=False)),
                ('url', models.CharField(max_length=100)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'counter',
                'ordering': ['timestamp'],
            },
            bases=(models.Model,),
        ),
    ]
