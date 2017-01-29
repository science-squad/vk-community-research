# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-29 17:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('communities', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='VkPerson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vk_id', models.PositiveIntegerField(verbose_name='vk id')),
                ('first_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='last name')),
                ('sex', models.IntegerField(null=True, verbose_name='sex')),
            ],
            options={
                'verbose_name_plural': 'vk persons',
                'verbose_name': 'vk person',
            },
        ),
        migrations.AlterField(
            model_name='vkcommunity',
            name='member_list_length',
            field=models.PositiveIntegerField(null=True, verbose_name='loaded member list length'),
        ),
    ]
