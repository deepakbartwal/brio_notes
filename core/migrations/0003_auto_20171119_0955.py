# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20171001_0007'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stream',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=10, db_index=True)),
            ],
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['category']},
        ),
        migrations.AlterModelOptions(
            name='notes',
            options={'ordering': ['title']},
        ),
        migrations.AlterModelOptions(
            name='questionpaper',
            options={'ordering': ['title']},
        ),
        migrations.RemoveField(
            model_name='notes',
            name='category',
        ),
        migrations.RemoveField(
            model_name='questionpaper',
            name='category',
        ),
        migrations.AddField(
            model_name='notes',
            name='meta',
            field=models.CharField(max_length=255, blank=True),
        ),
    ]
