# coding: utf-8
from django.contrib import admin
from sistema_pedidos.models import DadosPessoais, Loja, LojaUsuario, Recebimento
from sistema_pedidos.models import Categoria, Produto, Pedido, ItemPedido, Tipo
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class EmailRequiredMixin(object):
    def __init__(self, *args, **kwargs):
        super(EmailRequiredMixin, self).__init__(*args, **kwargs)
        # make user email field required
        self.fields['email'].required = True


class MyUserCreationForm(EmailRequiredMixin, UserCreationForm):
    pass


class MyUserChangeForm(EmailRequiredMixin, UserChangeForm):
    pass



class TipoInline(admin.StackedInline):
    model = Tipo
    can_delete = False
    verbose_name_plural = 'Tipo'

# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (TipoInline, )
    form = MyUserChangeForm
    add_form = MyUserCreationForm
    add_fieldsets = ((None, {'fields': ('username', 'email',
                                        'password1', 'password2'), 'classes': ('wide',)}),)
    

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
