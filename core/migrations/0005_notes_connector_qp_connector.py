# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20171119_1016'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notes_Connector',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('category', models.ForeignKey(to='core.Category')),
                ('notes', models.ForeignKey(to='core.Notes')),
                ('stream', models.ForeignKey(to='core.Stream')),
            ],
            options={
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='QP_Connector',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('category', models.ForeignKey(to='core.Category')),
                ('ques_paper', models.ForeignKey(to='core.QuestionPaper')),
                ('stream', models.ForeignKey(to='core.Stream')),
            ],
            options={
                'ordering': ['title'],
            },
        ),
    ]
