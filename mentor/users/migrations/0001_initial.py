# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(verbose_name='password', max_length=128)),
                ('last_login', models.DateTimeField(verbose_name='last login', default=django.utils.timezone.now)),
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('username', models.CharField(db_index=True, max_length=100, unique=True)),
                ('email', models.EmailField(max_length=100)),
                ('first_name', models.CharField(max_length=30, blank=True)),
                ('last_name', models.CharField(max_length=30, blank=True)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('is_student', models.BooleanField(default=True)),
                ('is_mentor', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'user',
            },
            bases=(models.Model,),
        ),
    ]
