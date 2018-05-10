# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-05-10 16:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='People',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fenzu', models.CharField(choices=[('佳佳', '佳佳'), ('木木', '木木'), ('绾绾', '绾绾')], max_length=20, null=True, verbose_name='所属分组')),
                ('title', models.CharField(max_length=256, null=True, verbose_name='昵称')),
                ('content', models.IntegerField(default='0', null=True, verbose_name='未交次数')),
                ('shifouchoucha', models.CharField(choices=[('是', '是'), ('否', '否')], default='是', max_length=10, null=True, verbose_name='是否抽查')),
            ],
        ),
    ]
