from rest_framework import viewsets
from lavajato.models import Cliente, Veiculo
from lavajato.serializer import ClienteSerializer, VeiculoSerializer

from django.http import JsonResponse

class ClientesViewSet(viewsets.ModelViewSet):
    """Exibindo todos os alunos e alunas"""
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class VeiculosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os cursos"""
    queryset = Veiculo.objects.all()
    serializer_class = VeiculoSerializer