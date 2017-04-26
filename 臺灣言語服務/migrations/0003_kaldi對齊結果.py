# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-26 11:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('臺灣言語資料庫', '0007_auto_20161121_2017'),
        ('臺灣言語服務', '0002_auto_20170426_1407'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kaldi對齊結果',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('對齊好猶未', models.BooleanField(default=False)),
                ('對齊出問題', models.BooleanField(default=False)),
                ('欲切開的文本', models.TextField()),
                ('影音', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='Kaldi對齊結果', to='臺灣言語資料庫.影音表')),
            ],
        ),
    ]
