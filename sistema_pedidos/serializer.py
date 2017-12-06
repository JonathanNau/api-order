# coding: utf-8

from rest_framework import serializers
from .models import DadosPessoais

from .models import Loja, LojaUsuario, Recebimento, Categoria, Produto, Pedido, ItemPedido, Tipo
from django.contrib.auth.models import User

from django.contrib.auth.hashers import make_password, is_password_usable

class Base64ImageField(serializers.ImageField):
    """
    A Django REST framework field for handling image-uploads through raw post data.
    It uses base64 for encoding and decoding the contents of the file.

    Heavily based on
    https://github.com/tomchristie/django-rest-framework/pull/1268

    Updated for Django REST framework 3.
    """

    def to_internal_value(self, data):
        from django.core.files.base import ContentFile
        import base64
        import six
        import uuid

        # Check if this is a base64 string
        if isinstance(data, six.string_types):
            # Check if the base64 string is in the "data:" format
            if 'data:' in data and ';base64,' in data:
                # Break out the header from the base64 content
                header, data = data.split(';base64,')

            # Try to decode the file. Return validation error if it fails.
            try:
                decoded_file = base64.b64decode(data)
            except TypeError:
                self.fail('invalid_image')

            # Generate file name:
            file_name = str(uuid.uuid4())[:12] # 12 characters are more than enough.
            # Get the file name extension:
            file_extension = self.get_file_extension(file_name, decoded_file)

            complete_file_name = "%s.%s" % (file_name, file_extension, )

            data = ContentFile(decoded_file, name=complete_file_name)

        return super(Base64ImageField, self).to_internal_value(data)

    def get_file_extension(self, file_name, decoded_file):
        import imghdr

        extension = imghdr.what(file_name, decoded_file)
        extension = "jpg" if extension == "jpeg" else extension

        return extension

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
        fields = ['id', 'username', 'first_name', 'email', 'password', 'is_active', 'codigo']
    
    def create(self, validated_data):
        profile_data = validated_data.pop('userprofile', None)
        validated_data['password'] = make_password(validated_data['password'])
        user = super(UsuariosSerializer, self).create(validated_data)
        self.update_or_create_profile(user, profile_data)
        return user
    
    def update(self, instance, validated_data):
        profile_data = validated_data.pop('userprofile', None)
        if is_password_usable(validated_data['password']):
            pass
        else: 
            validated_data['password'] = make_password(validated_data['password'])
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
    foto = Base64ImageField(
        max_length=None, use_url=True,
    )
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
        instance.descricao = validated_data.pop('descricao')
        instance.valor = validated_data.pop('valor')
        instance.foto = validated_data.pop('foto')
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

class ItemPedidoSerializer2(serializers.ModelSerializer):
    produto = serializers.PrimaryKeyRelatedField(
        queryset=Produto.objects.all(), write_only=True)
    pedido = serializers.PrimaryKeyRelatedField(
        queryset=Pedido.objects.all(), write_only=True)
    class Meta:
        model = ItemPedido
        depth = 1
        fields = ['id', 'pedido', 'produto', 'valor', 'quantidade']
    '''
    def create(self, request, *args, **kwargs):
        data = request.data.get("produtos") if 'produtos' in request.data else request.data
        many = isinstance(data, list)
        print (data, many)
        serializer = self.get_serializer(data=data, many=many)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    '''


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

