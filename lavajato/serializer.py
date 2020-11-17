from rest_framework import serializers
from lavajato.models import Cliente, Veiculo


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['id', 'nome', 'email', 'cpf', 'telefone']


class VeiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Veiculo
        fields = ['id', 'placa', 'ano', 'modelo', 'cor', 'descricao', 'cliente']

class ListaVeiculosClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Veiculo
        fields = ['placa', 'modelo']

class ListaClientesCadastradosVeiculoSerializer(serializers.ModelSerializer):
    cliente_id = serializers.ReadOnlyField(source='cliente.id')
    cliente_nome = serializers.ReadOnlyField(source='cliente.nome')
    cliente_cpf = serializers.ReadOnlyField(source='cliente.cpf')
    class Meta:
        model = Veiculo
        fields = ['cliente_id', 'cliente_nome', 'cliente_cpf']