from .serializer import UsuariosSerializer, LojasSerializer, LojaUsuarioSerializer, RecebimentoSerializer, CategoriaSerializer, ProdutoSerializer, PedidoSerializer, ItemPedidoSerializer, ItemPedidoSerializer2, new_new
from .models import Loja, LojaUsuario, Recebimento, Categoria, Produto, Pedido, ItemPedido
from django.contrib.auth.models import User
from django.db.models import F
#excluir depois
from .models import DadosPessoais

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny

from rest_framework import status

from django.shortcuts import render


def portfolio_exibir(request):
    pessoa = DadosPessoais.objects.all()
    context = {'pessoa': pessoa}

    return render(request, 'portfolios/portfolio_exibir.html', context)

class UsuarioListView(APIView):
    serializer_class = UsuariosSerializer
    
    def get(self, request, format=None):
        serializer = self.serializer_class(User.objects.all(), many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_409_CONFLICT)

class UsuarioAdd(APIView):
    serializer_class = UsuariosSerializer
    permission_classes = (AllowAny,)
    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_409_CONFLICT)
class UsuarioView(APIView):

    def get(self, request, pk, format=None):
        user = User.objects.get(pk=pk)
        serializer = UsuariosSerializer(user)
        return Response(serializer.data)

    def delete(self, request, pk, format=None):
        event = User.objects.get(pk=pk)
        event.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def put(self, request, pk, format=None):
        user = User.objects.get(pk=pk)
        serializer = UsuariosSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LojaListView(APIView):
    serializer_class = LojasSerializer

    def get(self, request, format=None):
        serializer = self.serializer_class(Loja.objects.all(), many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_409_CONFLICT)

class LojaView(APIView):

    def get(self, request, pk, format=None):
        user = Loja.objects.get(pk=pk)
        serializer = LojasSerializer(user)
        return Response(serializer.data)

    def delete(self, request, pk, format=None):
        event = Loja.objects.get(pk=pk)
        event.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def put(self, request, pk, format=None):
        user = Loja.objects.get(pk=pk)
        serializer = LojasSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LojaUsuarioListView(APIView):
    serializer_class = LojaUsuarioSerializer

    def get(self, request, format=None):
        serializer = self.serializer_class(LojaUsuario.objects.all(), many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_409_CONFLICT)

class LojaUsuarioView(APIView):

    def get(self, request, pk, format=None):
        user = LojaUsuario.objects.get(usuario=pk)
        serializer = LojaUsuarioSerializer(user)
        return Response(serializer.data)

    def delete(self, request, pk, format=None):
        event = LojaUsuario.objects.get(pk=pk)
        event.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def put(self, request, pk, format=None):
        user = LojaUsuario.objects.get(pk=pk)
        serializer = LojaUsuarioSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    

class FuncionariosView(APIView):

    def get(self, request, pk, format=None):
        serializer = LojaUsuarioSerializer(LojaUsuario.objects.filter(loja=pk), many=True)
        return Response(serializer.data)
  

class RecebimentoListView(APIView):
    serializer_class = RecebimentoSerializer

    def get(self, request, format=None):
        serializer = self.serializer_class(Recebimento.objects.all(), many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_409_CONFLICT)

class RecebimentoView(APIView):

    def get(self, request, pk, format=None):
        user = Recebimento.objects.filter(loja=pk)
        serializer = RecebimentoSerializer(user, many=True)
        return Response(serializer.data)

    def delete(self, request, pk, format=None):
        event = Recebimento.objects.get(pk=pk)
        event.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def put(self, request, pk, format=None):
        user = Recebimento.objects.get(pk=pk)
        serializer = RecebimentoSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    

class CategoriaListView(APIView):
    serializer_class = CategoriaSerializer

    def get(self, request, format=None):
        serializer = self.serializer_class(Categoria.objects.all(), many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_409_CONFLICT)


class CategoriaView(APIView):

    def get(self, request, pk, format=None):
        serializer = CategoriaSerializer(Categoria.objects.filter(loja=pk), many=True)
        return Response(serializer.data)

    def delete(self, request, pk, format=None):
        event = Categoria.objects.get(pk=pk)
        event.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def put(self, request, pk, format=None):
        user = Categoria.objects.get(pk=pk)
        serializer = CategoriaSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    

class ProdutoListView(APIView):
    serializer_class = ProdutoSerializer

    def get(self, request, format=None):
        serializer = self.serializer_class(Produto.objects.all(), many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_409_CONFLICT)

class ProdutoCategoriaView(APIView):
    
    def get(self, request, pk, format=None):
        serializer = ProdutoSerializer(Produto.objects.filter(categoria=pk), many=True)
        return Response(serializer.data)

class ProdutoView(APIView):
    
    def get(self, request, pk, format=None):
        categoria_loja = Categoria.objects.filter(loja=pk)
        serializer = ProdutoSerializer(Produto.objects.filter(categoria__in=categoria_loja), many=True)
        return Response(serializer.data)

    def delete(self, request, pk, format=None):
        event = Produto.objects.get(pk=pk)
        event.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def put(self, request, pk, format=None):
        user = Produto.objects.get(pk=pk)
        serializer = ProdutoSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)   

class PedidoListView(APIView):
    serializer_class = PedidoSerializer

    def get(self, request, format=None):
        serializer = self.serializer_class(Pedido.objects.all(), many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_409_CONFLICT)


class PedidoView(APIView):

    def get(self, request, pk, format=None):
        user = Pedido.objects.get(pk=pk)
        serializer = PedidoSerializer(user)
        return Response(serializer.data)

    def delete(self, request, pk, format=None):
        event = Pedido.objects.get(pk=pk)
        event.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def put(self, request, pk, format=None):
        user = Pedido.objects.get(pk=pk)
        serializer = PedidoSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)   

class ItemPedidoListView(APIView):
    serializer_class = ItemPedidoSerializer

    def get(self, request, format=None):
        serializer = self.serializer_class(ItemPedido.objects.all(), many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_409_CONFLICT)


class ItemPedidoListView2(APIView):
    serializer_class = ItemPedidoSerializer2

    def post(self, request, format=None):
        for elem in request.data.get("produtos"):
            print(elem)
            serializer = self.serializer_class(data=elem)
            if serializer.is_valid():
                serializer.save()
            else:
                return Response(serializer.errors, status=status.HTTP_409_CONFLICT)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ItemPedidoView(APIView):

    def get(self, request, pk, format=None):
        serializer = ItemPedidoSerializer(ItemPedido.objects.filter(pedido=pk), many=True)
        #user = ItemPedido.objects.get(pedido=pk)
        #serializer = ItemPedidoSerializer(user)
        return Response(serializer.data)

    def delete(self, request, pk, format=None):
        event = ItemPedido.objects.get(pk=pk)
        event.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def put(self, request, pk, format=None):
        user = ItemPedido.objects.get(pk=pk)
        serializer = ItemPedidoSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)   

class PedidoLojaView(APIView):

    def get(self, request, pk, format=None):
        serializer = PedidoSerializer(Pedido.objects.filter(loja=pk), many=True)
        return Response(serializer.data)

class PedidoClienteView(APIView):

    def get(self, request, pk, format=None):
        serializer = PedidoSerializer(Pedido.objects.filter(usuario=pk), many=True)
        return Response(serializer.data)

class new_newView(APIView):

    def get(self, request, pk, format=None):
        categoria_loja = Categoria.objects.filter(loja=pk)
        pr = Produto.objects.filter(categoria__in=categoria_loja)
        serializer = new_new(pr, many=True)
       
        #loja = Produto.objects.get(categoria.loja=pk)
        #user = Categoria.objects.all()
        #serializer = new_new(produtos, many=True)
        return Response(serializer.data)