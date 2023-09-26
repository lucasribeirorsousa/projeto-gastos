from django.db import models


class Gasto(models.Model):
    """ 
    Model para representar informações de gastos públicos.

    Este modelo armazena informações sobre os gastos públicos,
    incluindo detalhes sobre órgãos, categorias econômicas, empenhos,
    licitações, valores empenhados, valores liquidados e valores pagos.
    """

    ano_movimentacao = models.DecimalField(max_digits=4, decimal_places=0)
    mes_movimentacao = models.DecimalField(max_digits=2, decimal_places=0)
    orgao_codigo = models.DecimalField(max_digits=10, decimal_places=0)
    orgao_nome = models.TextField()
    unidade_codigo = models.DecimalField(max_digits=10, decimal_places=0)
    unidade_nome = models.TextField()
    categoria_economica_codigo = models.DecimalField(max_digits=10, decimal_places=0)
    categoria_economica_nome = models.TextField()
    grupo_despesa_codigo = models.DecimalField(max_digits=10, decimal_places=0)
    grupo_despesa_nome = models.TextField()
    modalidade_aplicacao_codigo = models.DecimalField(max_digits=10, decimal_places=0)
    modalidade_aplicacao_nome = models.TextField()
    elemento_codigo = models.DecimalField(max_digits=10, decimal_places=0)
    elemento_nome = models.TextField()
    subelemento_codigo = models.DecimalField(max_digits=10, decimal_places=0)
    subelemento_nome = models.TextField()
    funcao_codigo = models.DecimalField(max_digits=10, decimal_places=0)
    funcao_nome = models.TextField()
    subfuncao_codigo = models.DecimalField(max_digits=10, decimal_places=0)
    subfuncao_nome = models.TextField()
    programa_codigo = models.DecimalField(max_digits=10, decimal_places=0)
    programa_nome = models.TextField()
    acao_codigo = models.DecimalField(max_digits=10, decimal_places=0)
    acao_nome = models.TextField()
    fonte_recurso_codigo = models.DecimalField(max_digits=10, decimal_places=0)
    fonte_recurso_nome = models.TextField()
    empenho_ano = models.DecimalField(max_digits=4, decimal_places=0)
    empenho_modalidade_nome = models.TextField()
    empenho_modalidade_codigo = models.DecimalField(max_digits=10, decimal_places=0)
    empenho_numero = models.DecimalField(max_digits=10, decimal_places=0)
    subempenho = models.DecimalField(max_digits=15, decimal_places=2)
    indicador_subempenho = models.TextField()
    credor_codigo = models.DecimalField(max_digits=10, decimal_places=0)
    credor_nome = models.TextField()
    modalidade_licitacao_codigo = models.DecimalField(max_digits=10, decimal_places=0)
    modalidade_licitacao_nome = models.TextField()
    valor_empenhado = models.DecimalField(max_digits=15, decimal_places=2)
    valor_liquidado = models.DecimalField(max_digits=15, decimal_places=2)
    valor_pago = models.DecimalField(max_digits=15, decimal_places=2)

    def __str__(self):
        return f"{self.orgao_nome} - {self.ano_movimentacao}/{self.mes_movimentacao}"

    class Meta:
        verbose_name = "Gasto"
        verbose_name_plural = "Gastos"
