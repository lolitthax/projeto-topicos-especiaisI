from rest_framework import serializers
from lavajato.models import Cliente, Veiculo

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['id', 'nome', 'email', 'cpf', 'telefone']

class VeiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Veiculo
        field = ['id', 'placa', 'ano', 'modelo', 'cor', 'descricao']