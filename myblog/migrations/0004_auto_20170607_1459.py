# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-07 06:59
from __future__ import unicode_literals

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0003_auto_20170606_1805'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='body',
            field=ckeditor_uploader.fields.RichTextUploadingField(verbose_name='正文'),
        ),
    ]
