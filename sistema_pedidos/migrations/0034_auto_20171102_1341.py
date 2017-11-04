# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-02 15:41
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sistema_pedidos', '0033_auto_20170908_1855'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tipo',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='userprofile', to=settings.AUTH_USER_MODEL),
        ),
    ]
