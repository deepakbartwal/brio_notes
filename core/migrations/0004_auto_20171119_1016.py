# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20171119_0955'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='stream',
            options={'ordering': ['title']},
        ),
    ]
