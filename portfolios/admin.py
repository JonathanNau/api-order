# coding: utf-8
from django.contrib import admin
from portfolios.models import DadosPessoais, Loja, LojaUsuario, Recebimento
from portfolios.models import Categoria, Produto, Pedido, ItemPedido

admin.site.register(DadosPessoais)
admin.site.register(Loja)
admin.site.register(LojaUsuario)
admin.site.register(Recebimento)
admin.site.register(Categoria)
admin.site.register(Produto)
admin.site.register(Pedido)
admin.site.register(ItemPedido)

