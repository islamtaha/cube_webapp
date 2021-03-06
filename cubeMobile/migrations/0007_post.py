# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-22 14:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cubeMobile', '0006_cubian_content'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='posts/%Y/%m/%d/')),
                ('content', models.CharField(max_length=400)),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
