# coding: utf-8

from rest_framework import serializers
from .models import DadosPessoais

from .models import Loja, LojaUsuario, Recebimento, Categoria, Produto, Pedido, ItemPedido, Tipo
from django.contrib.auth.models import User

class DadosPessoaisSerializer(serializers.ModelSerializer):

    class Meta:
        model = DadosPessoais
        depth = 1
        fields = ['id', 'name', 'adress', 'city', 'cep', 'phone', 'mobile']

class TipoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tipo
        fields = ['user','codigo']

class UsuariosSerializer(serializers.ModelSerializer):
    codigo = serializers.IntegerField(source='userprofile.codigo')
    #codigo = TipoSerializer(required=True)

    class Meta:
        model = User
        depth = 1
        fields = ['id', 'username', 'email', 'password', 'is_active', 'codigo']
    
    def create(self, validated_data):
        profile_data = validated_data.pop('userprofile', None)
        user = super(UsuariosSerializer, self).create(validated_data)
        self.update_or_create_profile(user, profile_data)
        return user
    
    def update(self, instance, validated_data):
        profile_data = validated_data.pop('userprofile', None)
        self.update_or_create_profile(instance, profile_data)
        return super(UsuariosSerializer, self).update(instance, validated_data)

    def update_or_create_profile(self, user, profile_data):
        # This always creates a Profile if the User is missing one;
        # change the logic here if that's not right for your app
        Tipo.objects.update_or_create(user=user, defaults=profile_data)
        
class LojasSerializer(serializers.ModelSerializer):

    class Meta:
        model = Loja
        depth = 1
        fields = ['id','nome', 'telefone', 'latitude', 'longitude', 'situacao']

class LojaUsuarioSerializer(serializers.ModelSerializer):
    loja1 = serializers.PrimaryKeyRelatedField(
        queryset=Loja.objects.all(), write_only=True)
    usuario1 = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), write_only=True)
    class Meta:
        model = LojaUsuario
        depth = 1
        fields = ['id','loja', 'usuario', 'loja1', 'usuario1',]

    def create(self, validated_data):
        child1 = validated_data.pop('usuario1')
        child2 = validated_data.pop('loja1')
        return LojaUsuario.objects.create(usuario=child1, loja=child2)

class RecebimentoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Recebimento
        depth = 1
        fields = ['id', 'loja', 'nome', 'situacao']

class CategoriaSerializer(serializers.ModelSerializer):
    #child = LojasSerializer(read_only=True) 
    loja1 = serializers.PrimaryKeyRelatedField(
        queryset=Loja.objects.all(), write_only=True)
    #post = serializers.IntegerField(source='loja.id')
    class Meta:
        model = Categoria
        depth = 1
        fields = ['id', 'loja', 'nome', 'situacao', 'loja1']
    def create(self, validated_data):
        child_data = validated_data.pop('loja1')
        return Categoria.objects.create(loja=child_data, **validated_data)

class ProdutoSerializer(serializers.ModelSerializer):
    categoria1 = serializers.PrimaryKeyRelatedField(
        queryset=Categoria.objects.all(), write_only=True)
    #categoria = CategoriaSerializer()
    class Meta:
        model = Produto
        depth = 1
        fields = ['id', 'categoria', 'nome', 'descricao', 'valor', 'data', 'situacao', 'foto', 'categoria1']
    
    def create(self, validated_data):
        child_data = validated_data.pop('categoria1')
        return Produto.objects.create(categoria=child_data, **validated_data)
    
    def update(self, instance, validated_data):
        instance.categoria = validated_data.pop('categoria1')
        instance.nome = validated_data.pop('nome')
        instance.valor = validated_data.pop('valor')
        instance.situacao = validated_data.pop('situacao')
        # ... plus any other fields you may want to update
        instance.save()
        return instance

class PedidoSerializer(serializers.ModelSerializer):
    usuario1 = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), write_only=True)
    loja1 = serializers.PrimaryKeyRelatedField(
        queryset=Loja.objects.all(), write_only=True)
    recebimento1 = serializers.PrimaryKeyRelatedField(
        queryset=Recebimento.objects.all(), write_only=True)
    class Meta:
        model = Pedido
        depth = 1
        fields = ['id', 'usuario', 'loja', 'recebimento', 'recebimento_valor', 'data', 'situacao', 'usuario1', 'loja1', 'recebimento1']

    def create(self, validated_data):
        child_data1 = validated_data.pop('usuario1')
        child_data2 = validated_data.pop('loja1')
        child_data3 = validated_data.pop('recebimento1')
        return Pedido.objects.create(usuario=child_data1, loja=child_data2, recebimento=child_data3, **validated_data)

class ItemPedidoSerializer(serializers.ModelSerializer):
    produto1 = serializers.PrimaryKeyRelatedField(
        queryset=Produto.objects.all(), write_only=True)
    pedido1 = serializers.PrimaryKeyRelatedField(
        queryset=Pedido.objects.all(), write_only=True)
    class Meta:
        model = ItemPedido
        depth = 1
        fields = ['id', 'pedido', 'produto', 'valor', 'quantidade', 'produto1', 'pedido1']
    
    def create(self, validated_data):
        child_data1 = validated_data.pop('produto1')
        child_data2 = validated_data.pop('pedido1')
        return ItemPedido.objects.create(produto=child_data1, pedido=child_data2, **validated_data)

class ProductSerializer(serializers.ModelSerializer):
    #loja = ProductVariantSerializer(source='product', many=True, read_only=True)
    class Meta:
        model = Produto
        fields = ('nome', 'categoria')

class CategorySerializer(serializers.ModelSerializer):
    #products = ProductSerializer(source='categoria', many=True, read_only=True)
    class Meta:
        model = Categoria
        fields = ('nome')

class new_new(serializers.ModelSerializer):
    #products = CategorySerializer(source='categoria', many=True, read_only=True)
    class Meta:
        model = Produto
        fields = ('id', 'nome', 'categoria')