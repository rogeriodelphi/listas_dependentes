from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy

from .models import Cliente, Cidade
from .forms import ClienteForm


class listar_clientes(ListView):
    model = Cliente
    context_object_name = 'people'


class adicionar_cliente(CreateView):
    model = Cliente
    form_class = ClienteForm
    success_url = reverse_lazy('listar_clientes')


class editar_cliente(UpdateView):
    model = Cliente
    form_class = ClienteForm
    success_url = reverse_lazy('listar_clientes')


def ajax_carregar_cidades(request):
    uf_id = request.GET.get('uf')
    cidades = Cidade.objects.filter(uf_id=uf_id).order_by('nome')
    return render(request, 'clientes/opcao_listar_cidades.html', {'cidades': cidades})
