# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-09 14:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sistema_pedidos', '0042_produto_descricao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='descricao',
            field=models.CharField(default=b'', max_length=1000),
        ),
    ]
