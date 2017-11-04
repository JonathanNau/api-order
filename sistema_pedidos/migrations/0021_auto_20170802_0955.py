# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-02 12:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sistema_pedidos', '0020_loja_usuario'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name=b'Nome')),
                ('situacao', models.BooleanField(verbose_name=b'Ativo')),
            ],
        ),
        migrations.CreateModel(
            name='ItemPedido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.DecimalField(decimal_places=2, max_digits=5, verbose_name=b'Valor')),
                ('quantidade', models.IntegerField(verbose_name=b'Quantidade')),
            ],
        ),
        migrations.CreateModel(
            name='LojaUsuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recebimento_valor', models.CharField(max_length=100, verbose_name=b'Valor')),
                ('data', models.DateField(verbose_name=b'Data')),
                ('situacao', models.BooleanField(verbose_name=b'Ativo')),
            ],
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name=b'Nome')),
                ('valor', models.DecimalField(decimal_places=2, max_digits=5, verbose_name=b'Valor')),
                ('data', models.DateField(verbose_name=b'Data')),
                ('situacao', models.BooleanField(verbose_name=b'Ativo')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sistema_pedidos.Categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Recebimentos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name=b'Nome')),
                ('situacao', models.BooleanField(verbose_name=b'Ativo')),
            ],
        ),
        migrations.AlterField(
            model_name='loja',
            name='situacao',
            field=models.BooleanField(verbose_name=b'Ativo'),
        ),
        migrations.AddField(
            model_name='recebimentos',
            name='loja',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sistema_pedidos.Loja'),
        ),
        migrations.AddField(
            model_name='pedido',
            name='loja',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sistema_pedidos.Loja'),
        ),
        migrations.AddField(
            model_name='pedido',
            name='recebimento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sistema_pedidos.Recebimentos'),
        ),
        migrations.AddField(
            model_name='pedido',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sistema_pedidos.Usuario'),
        ),
        migrations.AddField(
            model_name='lojausuario',
            name='loja',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sistema_pedidos.Loja'),
        ),
        migrations.AddField(
            model_name='lojausuario',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sistema_pedidos.Usuario'),
        ),
        migrations.AddField(
            model_name='itempedido',
            name='pedido',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sistema_pedidos.Pedido'),
        ),
        migrations.AddField(
            model_name='itempedido',
            name='produto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sistema_pedidos.Produto'),
        ),
        migrations.AddField(
            model_name='categoria',
            name='loja',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sistema_pedidos.Loja'),
        ),
    ]