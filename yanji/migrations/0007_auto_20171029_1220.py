# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-10-29 04:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yanji', '0006_auto_20171029_1141'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tag',
            options={'verbose_name': '\u6f14\u6280\u6807\u7b7e', 'verbose_name_plural': '\u6f14\u6280\u6807\u7b7e'},
        ),
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(max_length=100, verbose_name='\u6f14\u6280\u6807\u7b7e'),
        ),
    ]
