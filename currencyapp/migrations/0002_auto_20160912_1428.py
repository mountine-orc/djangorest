# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-12 11:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('currencyapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rate',
            name='currency',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rates', to='currencyapp.Currency'),
        ),
        migrations.AlterField(
            model_name='rate',
            name='date',
            field=models.DateField(verbose_name='date'),
        ),
        migrations.AlterUniqueTogether(
            name='rate',
            unique_together=set([('currency', 'date')]),
        ),
    ]
