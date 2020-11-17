from django.db import models

# Create your models here.
class Cliente(models.Model):
    nome = models.CharField(max_length=30)
    email = models.CharField(max_length=60)
    cpf = models.CharField(max_length=11)
    telefone = models.CharField(max_length=15)
    def __str__(self):
        return self.nome

class Veiculo(models.Model):
    placa = models.CharField(max_length=7)
    ano = models.IntegerField()
    modelo = models.CharField(max_length=30)
    cor = models.CharField(max_length=30)
    descricao = models.CharField(max_length=50)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    def __str__(self):
        return self.placa