# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='PrimaryConcernChoice',
            fields=[
                ('primary_concern_choice_id', models.AutoField(primary_key=True, serialize=False)),
                ('value', models.CharField(max_length=255)),
                ('rank', models.IntegerField()),
            ],
            options={
                'ordering': ['rank'],
                'db_table': 'primary_concern_choice',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Questionaire',
            fields=[
                ('questionaire_id', models.AutoField(primary_key=True, serialize=False)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('student_name', models.CharField(max_length=255, blank=True)),
                ('student_ID', models.DecimalField(max_digits=9, decimal_places=0, blank=True, null=True)),
                ('mentor_name', models.CharField(max_length=255, blank=True)),
                ('identity', models.CharField(max_length=255, blank=True)),
                ('on_behalf_of_student', models.CharField(max_length=255, blank=True)),
                ('UNST_course', models.CharField(max_length=255, blank=True)),
                ('type_of_course', models.CharField(max_length=255, blank=True)),
                ('primary_concern_other', models.TextField(blank=True)),
                ('primary_concern_details', models.TextField(blank=True)),
                ('step_taken', models.TextField(blank=True)),
                ('when_take_step', models.CharField(max_length=255, blank=True)),
                ('support_from_MAPS', models.TextField(blank=True)),
                ('contact_who', models.CharField(max_length=255, blank=True)),
                ('follow_up_email', models.EmailField(max_length=75, blank=True, null=True)),
                ('follow_up_phone', models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)),
                ('status', models.IntegerField(default=4, choices=[(2, 'Resolved'), (4, 'Unresolved')])),
                ('changed_on', models.DateTimeField(auto_now=True)),
                ('primary_concern', models.ManyToManyField(to='questionaire.PrimaryConcernChoice')),
                ('user', models.ForeignKey(to='users.User')),
            ],
            options={
                'ordering': ['created_on'],
                'db_table': 'questionaire',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='QuestionaireHistory',
            fields=[
                ('questionaire_history_id', models.AutoField(primary_key=True, serialize=False)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('action', models.IntegerField(choices=[(1, 'Viewed'), (2, 'Resolved'), (4, 'Unresolved')])),
                ('questionaire', models.ForeignKey(to='questionaire.Questionaire')),
                ('user', models.ForeignKey(to='users.User')),
            ],
            options={
                'ordering': ['-created_on'],
                'db_table': 'questionaire_history',
            },
            bases=(models.Model,),
        ),
    ]
