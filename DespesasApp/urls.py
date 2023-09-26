"""DespesasApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from gastos import views 
from django.shortcuts import redirect

urlpatterns = [
    path('', lambda request: redirect('despesas_por_mes/')),
    path('admin/', admin.site.urls),
    path('despesas_por_mes/', views.despesas_por_mes, name='despesas_por_mes'),
    path('despesas_por_categoria/', views.despesas_por_categoria, name='despesas_por_categoria'),
    path('fontes_de_dinheiro/', views.fontes_de_dinheiro, name='fontes_de_dinheiro'),
    path('todos_os_dados/', views.TodosOsDadosListView.as_view(), name='todos_os_dados'),
    path('adicionar_editar_dados/', views.AdicionarDadosView.as_view(), name='adicionar_editar_dados'),
    path('editar_dados/<int:pk>/', views.EditarDadosView.as_view(), name='editar_dados'),
    path('excluir_dados/<int:pk>/', views.ExcluirDadosView.as_view(), name='excluir_dados'),
    path('api/todos_os_dados/', views.GastoListCreateView.as_view(), name='api_todos_os_dados'),
    path('api/todos_os_dados/<int:pk>/', views.GastoRetrieveUpdateDestroyView.as_view(), name='api_detalhes_dados'),
]
