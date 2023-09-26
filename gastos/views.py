from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from django.views.generic import ListView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Gasto
from .serializers import GastoSerializer
from .forms import GastoForm
from django.db import models


def despesas_por_mes(request):
    # Query para calcular despesas totais por mês
    despesas = Gasto.objects.values('ano_movimentacao', 'mes_movimentacao').annotate(total_despesas=models.Sum('valor_pago'))
    
    # Convertendo dados de despesas para o contexto
    labels = [f"{despesa['ano_movimentacao']}/{despesa['mes_movimentacao']}" for despesa in despesas]
    total_pago = [despesa['total_despesas'] for despesa in despesas]

    # Contexto de dados para o front
    context = {
        'despesas': despesas,
        'labels': labels,
        'total_pago': total_pago,
    }

    return render(request, 'despesas/despesas_por_mes.html', context)


def despesas_por_categoria(request):
    # Query para calcular despesas por categoria
    despesas = Gasto.objects.values('categoria_economica_nome').annotate(total_despesas=models.Sum('valor_pago'))
    
    return render(request, 'despesas/despesas_por_categoria.html', {'despesas': despesas})


def fontes_de_dinheiro(request):
    # Query para calcular de onde vem o dinheiro agrupado por fonte
    fontes = Gasto.objects.values('fonte_recurso_nome').annotate(total_despesas=models.Sum('valor_pago'))
    
    return render(request, 'despesas/fontes_de_dinheiro.html', {'fontes': fontes})


class TodosOsDadosListView(ListView):
    model = Gasto
    template_name = 'despesas/todos_os_dados.html'
    context_object_name = 'gastos'
    paginate_by = 10 

class AdicionarDadosView(TemplateView):
    template_name = 'despesas/adicionar_editar_dados.html'


class EditarDadosView(UpdateView):
    model = Gasto
    template_name = 'despesas/adicionar_editar_dados.html'
    fields = '__all__'


class ExcluirDadosView(DeleteView):
    model = Gasto
    success_url = reverse_lazy('todos_os_dados')


class CustomPageNumberPagination(PageNumberPagination):
    page_size = 10  
    page_size_query_param = 'page_size'
    max_page_size = 100  


class GastoListCreateView(generics.ListCreateAPIView):
    queryset = Gasto.objects.all()
    serializer_class = GastoSerializer
    pagination_class = CustomPageNumberPagination


class GastoRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Gasto.objects.all()
    serializer_class = GastoSerializer
