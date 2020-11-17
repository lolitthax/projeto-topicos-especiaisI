from rest_framework import viewsets
from lavajato.models import Cliente, Veiculo
from lavajato.serializer import ClienteSerializer, VeiculoSerializer
from rest_framework import viewsets, generics
from lavajato.serializer import ClienteSerializer, VeiculoSerializer, ListaVeiculosClienteSerializer, ListaClientesCadastradosVeiculoSerializer

from django.http import JsonResponse

class ClientesViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class VeiculosViewSet(viewsets.ModelViewSet):
    queryset = Veiculo.objects.all()
    serializer_class = VeiculoSerializer


class ListaVeiculosClienteViewSet(generics.ListAPIView):
    """Exibindo as matriculas de um aluno"""
    def get_queryset(self):
        queryset = Veiculo.objects.filter(cliente_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListaVeiculosClienteSerializer

class ListaClientesCadastradosVeiculoViewset(generics.ListAPIView):
    """Exibindo alunos matriculados em um curso"""
    def get_queryset(self):
        queryset = Veiculo.objects.filter(id=self.kwargs['pk'])
        return queryset
    serializer_class = ListaVeiculosClienteSerializer
