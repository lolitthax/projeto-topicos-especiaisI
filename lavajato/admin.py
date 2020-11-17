from django.contrib import admin

from lavajato.models import Cliente, Veiculo
class Clientes(admin.ModelAdmin):
    list_display = ('id', 'nome', 'email', 'cpf', 'telefone')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)
    list_per_page = 20
admin.site.register(Cliente, Clientes)

class Veiculos(admin.ModelAdmin):
    list_display = ('id', 'placa', 'ano', 'modelo', 'cor', 'descricao','cliente')
    list_display_links = ('id', 'placa','cliente')
    search_fields = ('placa',)
    list_per_page = 20
admin.site.register(Veiculo, Veiculos)