# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-01 22:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sistema_pedidos', '0014_delete_usuarios'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=50, verbose_name=b'Tipo')),
                ('nome', models.CharField(max_length=50, verbose_name=b'Nome')),
                ('email', models.EmailField(max_length=254, verbose_name=b'Email')),
                ('teste1', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=6)),
            ],
        ),
    ]
