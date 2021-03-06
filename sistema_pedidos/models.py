# coding: utf-8
from django.db import models
from django.forms import ModelForm, PasswordInput
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
import uuid
import os
from django.contrib.auth.models import User
User._meta.get_field('email')._unique = True
User._meta.get_field('email').required = True
def get_file_path(instance, filename):
  ext = filename.split(".")[-1]
  filename = "%s.%s" % (uuid.uuid4(), ext)
  return os.path.join("produtos", filename)

def get_file_path_loja(instance, filename):
  ext = filename.split(".")[-1]
  filename = "%s.%s" % (uuid.uuid4(), ext)
  return os.path.join("lojas", filename)

class EmailBackend(ModelBackend):
    def authenticate(self, username=None, password=None, **kwargs):
        #UserModel = get_user_model()
        try:
            user = User.objects.get(email=username)
        except User.DoesNotExist:
            return None
        else:
            if user.check_password(password):
                return user
        return None

class Tipo(models.Model):
    user = models.OneToOneField(User, related_name='userprofile', on_delete=models.CASCADE)
    codigo = models.IntegerField(verbose_name='Tipo')

class DadosPessoais(models.Model):
    name = models.CharField(max_length=50, verbose_name='Nome')
    adress = models.CharField(max_length=100, verbose_name='Endereço')
    city = models.CharField(max_length=50, verbose_name='Cidade')
    cep = models.CharField(max_length=50, verbose_name='Cep')
    phone = models.CharField(max_length=20, verbose_name='Telefone')
    mobile = models.CharField(max_length=20, verbose_name='Celular')

    about = models.TextField(max_length=255, verbose_name='Sobre')
    data_nascimento = models.CharField(max_length=255, default='01 de janeiro de 2000', verbose_name='Data Nascimento')
    email = models.EmailField(verbose_name='Email')

    conhecimentos = models.TextField(max_length=255, verbose_name='Conhecimentos')
    github = models.CharField(max_length=100, default='http://github.com/SeuGit', verbose_name='Github')
    current_position = models.CharField(max_length=100, verbose_name='Cargo atual')
    empresa = models.CharField(max_length=100, verbose_name='Empresa')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Dados Pessoais'
        verbose_name_plural = 'Dados Pessoais'
'''
class Usuario(models.Model):
    tipo = models.CharField(max_length=50, verbose_name='Tipo')
    nome = models.CharField(max_length=50, verbose_name='Nome')
    email = models.EmailField(verbose_name='Email')
    senha = models.CharField(max_length=6, verbose_name='Senha')
    data = models.DateField(verbose_name='Data')
    situacao = models.BooleanField(verbose_name='Ativo')
    def __str__(self):
        return self.nome
'''
class Loja(models.Model):
    nome = models.CharField(max_length=100, verbose_name='Nome')
    telefone = models.IntegerField(verbose_name='Telefone')
    latitude = models.FloatField(max_length=50, verbose_name='Latitude')
    longitude = models.FloatField(max_length=50, verbose_name='Longitude')
    situacao = models.BooleanField(verbose_name='Ativo')
    foto = models.FileField(upload_to=get_file_path, default='sem_imagem.jpg')
    def __str__(self):
        return str(self.nome)

class LojaUsuario(models.Model):
    loja = models.ForeignKey(Loja, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        a = str(self.usuario) + ' - ' + str(self.loja)
        return a

class Recebimento(models.Model):
    loja = models.ForeignKey(Loja, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100, verbose_name='Nome')
    situacao = models.BooleanField(verbose_name='Ativo')
    def __str__(self):
        a = str(self.loja) + ' - ' + str(self.nome)
        return a

class Categoria(models.Model):
    loja = models.ForeignKey(Loja, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100, verbose_name='Nome')
    situacao = models.BooleanField(verbose_name='Ativo')
    def __str__(self):
        a = str(self.loja) + ' - ' + str(self.nome)
        return a

class Produto(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100, verbose_name='Nome')
    descricao = models.CharField(max_length=1000, default='')
    valor = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Valor')
    data = models.DateField(verbose_name='Data')
    situacao = models.BooleanField(verbose_name='Ativo')
    foto = models.FileField(upload_to=get_file_path, default='sem_imagem.jpg')
    def __str__(self):
        a = str(self.categoria.loja) + ' - ' + str(self.categoria.nome) + ' - ' + str(self.nome)
        return a

class Pedido(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    loja = models.ForeignKey(Loja, on_delete=models.CASCADE)
    recebimento = models.ForeignKey(Recebimento, on_delete=models.CASCADE)
    recebimento_valor = models.CharField(max_length=100, verbose_name='Valor')
    data = models.DateField(verbose_name='Data')
    situacao = models.CharField(max_length=100, verbose_name='Situação')
    def __str__(self):
        a = str(self.recebimento) + ' - ' + str(self.usuario) + ' - ' + str(self.data)
        return a

class ItemPedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    valor = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Valor')
    quantidade = models.IntegerField(verbose_name='Quantidade')
    def __str__(self):
        return str(self.pedido)
