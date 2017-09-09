# coding: utf-8
from django.contrib import admin
from portfolios.models import DadosPessoais, Loja, LojaUsuario, Recebimento
from portfolios.models import Categoria, Produto, Pedido, ItemPedido, Tipo
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

class TipoInline(admin.StackedInline):
    model = Tipo
    can_delete = False
    verbose_name_plural = 'Tipo'

# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (TipoInline, )

admin.site.unregister(User)
admin.site.register(User, UserAdmin)

admin.site.register(DadosPessoais)
admin.site.register(Loja)
admin.site.register(LojaUsuario)
admin.site.register(Recebimento)
admin.site.register(Categoria)
admin.site.register(Produto)
admin.site.register(Pedido)
admin.site.register(ItemPedido)

