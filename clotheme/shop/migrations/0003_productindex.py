# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-10 10:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_initialdata'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('Kids', 'Kids'), ('Men', 'Men'), ('Women', 'Women')], db_index=True, max_length=10),
        ),
    ]
