# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('category', models.CharField(blank=True, max_length=32, null=True, db_index=True, choices=[(b'undergraduate', b'Undergraduate'), (b'graduate', b'Graduate'), (b'post_graduate', b'Postgraduate')])),
                ('cat_type', models.CharField(max_length=255, db_index=True)),
                ('stream', models.CharField(db_index=True, max_length=8, null=True, blank=True)),
                ('degree_name', models.CharField(max_length=255, db_index=True)),
            ],
        ),
        migrations.CreateModel(
            name='Notes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255, db_index=True)),
                ('file', models.FileField(upload_to=b'notes')),
                ('category', models.ForeignKey(to='core.Category')),
            ],
        ),
        migrations.CreateModel(
            name='QuestionPaper',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255, db_index=True)),
                ('file', models.FileField(upload_to=b'notes')),
                ('is_solved', models.BooleanField(default=False)),
                ('category', models.ForeignKey(to='core.Category')),
            ],
        ),
    ]
