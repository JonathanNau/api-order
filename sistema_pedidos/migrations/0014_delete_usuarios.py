# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-01 22:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sistema_pedidos', '0013_usuarios'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Usuarios',
        ),
    ]