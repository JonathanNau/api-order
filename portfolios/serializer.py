# coding: utf-8

from rest_framework import serializers
from .models import DadosPessoais

from .models import Usuario, Loja, LojaUsuario, Recebimento, Categoria, Produto, Pedido, ItemPedido


class DadosPessoaisSerializer(serializers.ModelSerializer):

    class Meta:
        model = DadosPessoais
        depth = 1
        fields = ['id', 'name', 'adress', 'city', 'cep', 'phone', 'mobile']


class UsuariosSerializer(serializers.ModelSerializer):

    class Meta:
        model = Usuario
        depth = 1
        fields = ['id', 'nome', 'email', 'senha', 'data', 'situacao']
        
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
