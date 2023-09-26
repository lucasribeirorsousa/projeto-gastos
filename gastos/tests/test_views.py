from django.test import TestCase
from django.urls import reverse
from gastos.models import Gasto
from decimal import Decimal

class GastoViewsTestCase(TestCase):
    def setUp(self):
       Gasto.objects.create(
            ano_movimentacao=2023,
            mes_movimentacao=1,
            orgao_codigo=123,
            orgao_nome='Ministério da Saúde',
            unidade_codigo=456,
            unidade_nome='Unidade de Saúde',
            categoria_economica_codigo=789,
            categoria_economica_nome='Categoria Econômica',
            grupo_despesa_codigo=101,
            grupo_despesa_nome='Grupo de Despesa',
            modalidade_aplicacao_codigo=202,
            modalidade_aplicacao_nome='Modalidade de Aplicação',
            elemento_codigo=303,
            elemento_nome='Elemento',
            subelemento_codigo=404,
            subelemento_nome='Subelemento',
            funcao_codigo=505,
            funcao_nome='Função',
            subfuncao_codigo=606,
            subfuncao_nome='Subfunção',
            programa_codigo=707,
            programa_nome='Programa',
            acao_codigo=808,
            acao_nome='Ação',
            fonte_recurso_codigo=909,
            fonte_recurso_nome='Fonte de Recurso',
            empenho_ano=2023,
            empenho_modalidade_nome='Modalidade do Empenho',
            empenho_modalidade_codigo=111,
            empenho_numero=222,
            subempenho=Decimal('50.00'),
            indicador_subempenho='Indicador do Subempenho',
            credor_codigo=999,
            credor_nome='Credor',
            modalidade_licitacao_codigo=12345,
            modalidade_licitacao_nome='Modalidade da Licitação',
            valor_empenhado=Decimal('200.00'),
            valor_liquidado=Decimal('150.00'),
            valor_pago=Decimal('100.00')
        )

    def test_despesas_por_mes_view(self):
        url = reverse('despesas_por_mes')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_despesas_por_categoria_view(self):
        url = reverse('despesas_por_categoria')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_fontes_de_dinheiro_view(self):
        url = reverse('fontes_de_dinheiro')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_todos_os_dados_list_view(self):
        url = reverse('todos_os_dados')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['gastos'], Gasto.objects.all(), transform=lambda x: x)

    def test_adicionar_dados_view(self):
        url = reverse('adicionar_editar_dados')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_editar_dados_view(self):
        gasto = Gasto.objects.first()
        url = reverse('editar_dados', args=[gasto.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_excluir_dados_view(self):
        gasto = Gasto.objects.first()
        url = reverse('excluir_dados', args=[gasto.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_api_todos_os_dados_list_view(self):
        url = reverse('api_todos_os_dados')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'results')

    def test_api_detalhes_dados_retrieve_view(self):
        gasto = Gasto.objects.first()
        url = reverse('api_detalhes_dados', args=[gasto.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['id'], gasto.pk)
