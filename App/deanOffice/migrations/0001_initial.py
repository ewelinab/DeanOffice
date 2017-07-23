# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('employeeId', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('firstName', models.CharField(max_length=200)),
                ('lastName', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Numbers',
            fields=[
                ('numberId', models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('studentId', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('firstName', models.CharField(max_length=200)),
                ('lastName', models.CharField(max_length=200)),
                ('faculty', models.CharField(max_length=100)),
                ('groupId', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='numbers',
            name='studentId',
            field=models.ForeignKey(to='deanOffice.Student'),
        ),
    ]
