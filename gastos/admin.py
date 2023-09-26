from django.contrib import admin
from .models import Gasto

@admin.register(Gasto)
class GastoAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Gasto._meta.get_fields()]
    list_filter = ('ano_movimentacao', 'mes_movimentacao', 'orgao_nome')
    search_fields = ('orgao_nome', 'mes_movimentacao', 'categoria_economica_nome') 
