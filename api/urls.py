# coding: utf-8
from django.conf.urls import url
from sistema_pedidos.views import UsuarioListView, UsuarioView, LojaUsuarioListView, RecebimentoListView, CategoriaListView, ProdutoListView, PedidoListView, ItemPedidoListView
from sistema_pedidos.views import LojaListView, LojaView, LojaUsuarioView, RecebimentoView, CategoriaView, ProdutoView, PedidoView, ItemPedidoView, FuncionariosView, new_newView, ProdutoCategoriaView

from sistema_pedidos.views import UsuarioAdd
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_jwt.views import verify_jwt_token

helper_patterns = [
    url(r'^usuarios/$', UsuarioListView.as_view(), name='usuarios'),
    url(r'^usuarios/add/', UsuarioAdd.as_view(), name='usuarios_add'),
    url(r'^usuarios/(?P<pk>[0-9]+)/$', UsuarioView.as_view(), name='get_usuario'),
    url(r'^lojas/$', LojaListView.as_view(), name='lojas'),
    url(r'^lojas/(?P<pk>[0-9]+)/$', LojaView.as_view(), name='get_lojas'),
    url(r'^lojausuario/$', LojaUsuarioListView.as_view(), name='loja_usuario'),
    url(r'^lojausuario/(?P<pk>[0-9]+)/$', LojaUsuarioView.as_view(), name='get_lojas_usuario'),
    url(r'^funcionarios/(?P<pk>[0-9]+)/$', FuncionariosView.as_view(), name='get_lojas_usuario'),
    url(r'^recebimento/$', RecebimentoListView.as_view(), name='recebimento'),
    url(r'^recebimento/(?P<pk>[0-9]+)/$', RecebimentoView.as_view(), name='get_recebimento'),
    url(r'^categoria/$', CategoriaListView.as_view(), name='categoria'),
    url(r'^categoria/(?P<pk>[0-9]+)/$', CategoriaView.as_view(), name='get_categoria'),
    url(r'^produto/$', ProdutoListView.as_view(), name='produto'),
    url(r'^produto/(?P<pk>[0-9]+)/$', ProdutoView.as_view(), name='get_produto'),
    url(r'^pedido/$', PedidoListView.as_view(), name='pedido'),
    url(r'^pedido/(?P<pk>[0-9]+)/$', PedidoView.as_view(), name='get_pedido'),
    url(r'^itempedido/$', ItemPedidoListView.as_view(), name='itempedido'),
    url(r'^itempedido/(?P<pk>[0-9]+)/$', ItemPedidoView.as_view(), name='get_itempedido'),
    url(r'^new/(?P<pk>[0-9]+)/$', new_newView.as_view(), name='get_new'),
    url(r'^produto-categoria/(?P<pk>[0-9]+)/$', ProdutoCategoriaView.as_view(), name='get_produto_categoria'),
    url(r'^auth/token/', obtain_jwt_token),
    url(r'^api-token-verify/', verify_jwt_token),
]

urlpatterns = helper_patterns