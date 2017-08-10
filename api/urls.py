# coding: utf-8
from django.conf.urls import url
from portfolios.views import UsuarioListView, UsuarioView, LojaUsuarioListView, RecebimentoListView, CategoriaListView, ProdutoListView, PedidoListView, ItemPedidoListView
from portfolios.views import LojaListView, LojaView, LojaUsuarioView, RecebimentoView, CategoriaView, ProdutoView, PedidoView, ItemPedidoView

helper_patterns = [
    url(r'^usuarios/$', UsuarioListView.as_view(), name='usuarios'),
    url(r'^usuarios/(?P<pk>[0-9]+)/$', UsuarioView.as_view(), name='get_usuario'),
    url(r'^lojas/$', LojaListView.as_view(), name='lojas'),
    url(r'^lojas/(?P<pk>[0-9]+)/$', LojaView.as_view(), name='get_lojas'),
    url(r'^lojausuario/$', LojaUsuarioListView.as_view(), name='loja_usuario'),
    url(r'^lojausuario/(?P<pk>[0-9]+)/$', LojaUsuarioView.as_view(), name='get_lojas_usuario'),
    url(r'^recebimento/$', RecebimentoListView.as_view(), name='recebimento'),
    url(r'^recebimento/(?P<pk>[0-9]+)/$', RecebimentoView.as_view(), name='get_recebimento'),
    url(r'^categoria/$', CategoriaListView.as_view(), name='categoria'),
    url(r'^categoria/(?P<pk>[0-9]+)/$', CategoriaView.as_view(), name='get_categoria'),
    url(r'^produto/$', CategoriaListView.as_view(), name='produto'),
    url(r'^produto/(?P<pk>[0-9]+)/$', CategoriaView.as_view(), name='get_produto'),
    url(r'^pedido/$', PedidoListView.as_view(), name='pedido'),
    url(r'^pedido/(?P<pk>[0-9]+)/$', PedidoView.as_view(), name='get_pedido'),
    url(r'^itempedido/$', ItemPedidoListView.as_view(), name='itempedido'),
    url(r'^itempedido/(?P<pk>[0-9]+)/$', ItemPedidoView.as_view(), name='get_itempedido')
]

urlpatterns = helper_patterns