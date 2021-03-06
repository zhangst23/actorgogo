# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-10-29 09:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('yanji', '0011_auto_20171029_1727'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drama',
            name='dramatype',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='yanji.Dramatype', verbose_name='\u5267\u672c\u7c7b\u578b'),
        ),
        migrations.AlterField(
            model_name='drama',
            name='movietv',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='yanji.Movietv', verbose_name='\u5f71\u89c6\u5267'),
        ),
        migrations.AlterField(
            model_name='drama',
            name='taici',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='yanji.Taici', verbose_name='\u53f0\u8bcd'),
        ),
        migrations.AlterField(
            model_name='movietv',
            name='movietype',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='yanji.Movietype', verbose_name='\u5f71\u89c6\u5267\u7c7b\u578b'),
        ),
        migrations.AlterField(
            model_name='taici',
            name='movietv',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='yanji.Movietv', verbose_name='\u5f71\u89c6\u5267'),
        ),
    ]
