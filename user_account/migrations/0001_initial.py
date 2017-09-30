# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(db_index=True, max_length=255, blank=True)),
                ('meta', models.TextField(blank=True)),
                ('language', models.CharField(db_index=True, max_length=255, blank=True)),
                ('location', models.CharField(db_index=True, max_length=255, blank=True)),
                ('gender', models.CharField(blank=True, max_length=6, null=True, db_index=True, choices=[(b'm', b'Male'), (b'f', b'Female'), (b'o', b'Other')])),
                ('level_of_education', models.CharField(blank=True, max_length=6, null=True, db_index=True, choices=[(b'p', b'Doctorate'), (b'm', b"Master's or professional degree"), (b'b', b"Bachelor's degree"), (b'a', b'Associate degree'), (b'hs', b'Secondary/high school'), (b'jhs', b'Junior secondary/junior high/middle school'), (b'el', b'Elementary/primary school'), (b'none', b'No Formal Education'), (b'other', b'Other Education')])),
                ('state', models.CharField(blank=True, max_length=6, null=True, db_index=True, choices=[(b'AP', b'Andhra Pradesh'), (b'AR', b'Arunachal Pradesh'), (b'AS', b'Assam'), (b'BR', b'Bihar'), (b'CG', b'Chhattisgarh'), (b'CHGH', b'Chandigarh'), (b'DN', b'Dadra and Nagar Haveli'), (b'DD', b'Daman and Diu'), (b'DL', b'Delhi'), (b'GA', b'Goa'), (b'GJ', b'Gujarat'), (b'HR', b'Haryana'), (b'HP', b'Himachal Pradesh'), (b'JK', b'Jammu and Kashmir'), (b'JH', b'Jharkhand'), (b'KA', b'Karnataka'), (b'KL', b'Kerala'), (b'MP', b'Madhya Pradesh'), (b'MH', b'Maharashtra'), (b'MN', b'Manipur'), (b'ML', b'Meghalaya'), (b'MZ', b'Mizoram'), (b'NL', b'Nagaland'), (b'OD', b'Odisha'), (b'PB', b'Punjab'), (b'PY', b'Pondicherry'), (b'RJ', b'Rajasthan'), (b'SK', b'Sikkim'), (b'TN', b'Tamil Nadu'), (b'TR', b'Tripura'), (b'UP', b'Uttar Pradesh'), (b'UK', b'Uttarakhand'), (b'WB', b'West Bengal')])),
                ('city', models.CharField(db_index=True, max_length=255, blank=True)),
                ('school_board', models.CharField(db_index=True, max_length=255, blank=True)),
                ('grad_university', models.CharField(db_index=True, max_length=255, blank=True)),
                ('post_grad_university', models.CharField(db_index=True, max_length=255, blank=True)),
                ('user', models.OneToOneField(related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'auth_userprofile',
            },
        ),
    ]
