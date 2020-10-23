from django.urls import path

from . import views

urlpatterns = [
    path('', views.listar_clientes.as_view(), name='listar_clientes'),
    path('adicionar/', views.adicionar_cliente.as_view(), name='adicionar_cliente'),
    path('<int:pk>/', views.editar_cliente.as_view(), name='editar_cliente'),
    path('ajax/carregar-cidades/', views.ajax_carregar_cidades, name='ajax_carregar_cidades'),
]
