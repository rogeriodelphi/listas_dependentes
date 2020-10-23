from django.contrib import admin

from clientes.models import Estado, Cidade, Cliente


@admin.register(Cidade)
class CidadeAdmin(admin.ModelAdmin):
    list_display = ('id', 'uf', 'nome')

@admin.register(Estado)
class EstadoAdmin(admin.ModelAdmin):
    list_display = ('id', 'uf', 'nome',)

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'data_nascimento', 'uf', 'cidade')

