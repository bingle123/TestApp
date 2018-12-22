# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('task_id', models.IntegerField(verbose_name='\u4efb\u52a1ID')),
                ('task_name', models.CharField(max_length=64, verbose_name='\u4efb\u52a1\u540d\u79f0\u4eba')),
                ('task_time', models.CharField(max_length=64, verbose_name='\u4efb\u52a1\u65f6\u95f4')),
            ],
        ),
    ]
