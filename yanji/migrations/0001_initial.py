# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-10-28 10:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='\u6f14\u5458')),
                ('touxiang', models.ImageField(blank=True, null=True, upload_to='yanyuan_tx', verbose_name='\u5934\u50cf')),
                ('ctime', models.DateTimeField(default=django.utils.timezone.now, null=True, verbose_name='\u6dfb\u52a0\u65f6\u95f4')),
            ],
            options={
                'verbose_name': '\u6f14\u5458',
                'verbose_name_plural': '\u6f14\u5458',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='\u5206\u7c7b')),
            ],
            options={
                'verbose_name': '\u5206\u7c7b',
                'verbose_name_plural': '\u5206\u7c7b',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='\u6807\u7b7e')),
            ],
            options={
                'verbose_name': '\u6807\u7b7e',
                'verbose_name_plural': '\u6807\u7b7e',
            },
        ),
        migrations.CreateModel(
            name='Yanji',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='\u6807\u9898')),
                ('content', models.TextField(verbose_name='\u5185\u5bb9')),
                ('fengmian', models.ImageField(blank=True, null=True, upload_to='yanji_fengmian', verbose_name='\u5c01\u9762\u56fe')),
                ('video', models.URLField(default='www.actorgogo.com', verbose_name='\u89c6\u9891\u5730\u5740')),
                ('ctime', models.DateTimeField(default=django.utils.timezone.now, null=True, verbose_name='\u6dfb\u52a0\u65f6\u95f4')),
                ('actors', models.ManyToManyField(blank=True, to='yanji.Author')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='yanji.Category')),
                ('tag', models.ManyToManyField(blank=True, to='yanji.Tag')),
            ],
            options={
                'verbose_name': '\u6f14\u6280',
                'verbose_name_plural': '\u6f14\u6280',
            },
        ),
    ]
