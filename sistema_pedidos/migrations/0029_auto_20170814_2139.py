# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-15 00:39
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sistema_pedidos', '0028_auto_20170814_2134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lojausuario',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]