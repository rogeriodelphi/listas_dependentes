from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy
from .models import Cliente

class PersonListView(ListView):
    model = Cliente
    context_object_name = 'cliente'

class PersonCreateView(CreateView):
    model = Cliente
    fields = ('nome', 'data_nascimento', 'endereco', 'cidade')
    success_url = reverse_lazy('person_changelist')

class PersonUpdateView(UpdateView):
    model = Cliente
    fields = ('nome', 'data_nascimento', 'endereco', 'cidade')
    success_url = reverse_lazy('person_changelist')