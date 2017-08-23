# coding: utf-8

from rest_framework import serializers
from .models import DadosPessoais

from .models import Loja, LojaUsuario, Recebimento, Categoria, Produto, Pedido, ItemPedido
from django.contrib.auth.models import User

class DadosPessoaisSerializer(serializers.ModelSerializer):

    class Meta:
        model = DadosPessoais
        depth = 1
        fields = ['id', 'name', 'adress', 'city', 'cep', 'phone', 'mobile']


class UsuariosSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        depth = 1
        fields = ['id', 'username', 'email', 'password', 'is_active']
        
class LojasSerializer(serializers.ModelSerializer):

    class Meta:
        model = Loja
        depth = 1
        fields = ['id','nome', 'telefone', 'latitude', 'longitude', 'situacao']

class LojaUsuarioSerializer(serializers.ModelSerializer):

    class Meta:
        model = LojaUsuario
        depth = 1
        fields = ['id','loja', 'usuario']

class RecebimentoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Recebimento
        depth = 1
        fields = ['id', 'loja', 'nome', 'situacao']

class CategoriaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Categoria
        depth = 1
        fields = ['id', 'loja', 'nome', 'situacao']

class ProdutoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Produto
        depth = 1
        fields = ['id', 'categoria', 'nome', 'valor', 'data', 'situacao']

class PedidoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pedido
        depth = 1
        fields = ['id', 'usuario', 'loja', 'recebimento', 'recebimento_valor', 'data', 'situacao']

class ItemPedidoSerializer(serializers.ModelSerializer):

    class Meta:
        model = ItemPedido
        depth = 1
        fields = ['id', 'pedido', 'produto', 'valor', 'quantidade']
