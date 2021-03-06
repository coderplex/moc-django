# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-06-06 14:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_MST_NewsArticle',
            fields=[
                ('articleId', models.AutoField(primary_key=True, serialize=False)),
                ('author', models.CharField(max_length=30)),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=250)),
                ('url', models.CharField(max_length=50)),
                ('urlToImage', models.CharField(max_length=80)),
                ('publishedAt', models.DateField()),
            ],
        ),
    ]
