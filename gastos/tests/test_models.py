import pytest
from gastos.models import Gasto

# Função para criar um objeto Gasto
def create_gasto(
    ano_movimentacao=2023,
    mes_movimentacao=1,
    orgao_codigo=123,
    orgao_nome='Ministério da Saúde',
    unidade_codigo=456,
    unidade_nome='Unidade de Saúde',
    categoria_economica_codigo=789,
    categoria_economica_nome='Categoria Econômica',
    grupo_despesa_codigo=1011,
    grupo_despesa_nome='Grupo Despesa',
    modalidade_aplicacao_codigo=1213,
    modalidade_aplicacao_nome='Modalidade Aplicação',
    elemento_codigo=1415,
    elemento_nome='Elemento',
    subelemento_codigo=1617,
    subelemento_nome='Subelemento',
    funcao_codigo=1819,
    funcao_nome='Função',
    subfuncao_codigo=2021,
    subfuncao_nome='Subfunção',
    programa_codigo=2223,
    programa_nome='Programa',
    acao_codigo=2425,
    acao_nome='Ação',
    fonte_recurso_codigo=2627,
    fonte_recurso_nome='Fonte Recurso',
    empenho_ano=2023,
    empenho_modalidade_nome='Modalidade',
    empenho_modalidade_codigo=2829,
    empenho_numero=3031,
    subempenho=1234.56,
    indicador_subempenho='Indicador',
    credor_codigo=3233,
    credor_nome='Credor',
    modalidade_licitacao_codigo=3435,
    modalidade_licitacao_nome='Modalidade Licitação',
    valor_empenhado=5678.90,
    valor_liquidado=4321.09,
    valor_pago=8765.43
):
    return Gasto.objects.create(
        ano_movimentacao=ano_movimentacao,
        mes_movimentacao=mes_movimentacao,
        orgao_codigo=orgao_codigo,
        orgao_nome=orgao_nome,
        unidade_codigo=unidade_codigo,
        unidade_nome=unidade_nome,
        categoria_economica_codigo=categoria_economica_codigo,
        categoria_economica_nome=categoria_economica_nome,
        grupo_despesa_codigo=grupo_despesa_codigo,
        grupo_despesa_nome=grupo_despesa_nome,
        modalidade_aplicacao_codigo=modalidade_aplicacao_codigo,
        modalidade_aplicacao_nome=modalidade_aplicacao_nome,
        elemento_codigo=elemento_codigo,
        elemento_nome=elemento_nome,
        subelemento_codigo=subelemento_codigo,
        subelemento_nome=subelemento_nome,
        funcao_codigo=funcao_codigo,
        funcao_nome=funcao_nome,
        subfuncao_codigo=subfuncao_codigo,
        subfuncao_nome=subfuncao_nome,
        programa_codigo=programa_codigo,
        programa_nome=programa_nome,
        acao_codigo=acao_codigo,
        acao_nome=acao_nome,
        fonte_recurso_codigo=fonte_recurso_codigo,
        fonte_recurso_nome=fonte_recurso_nome,
        empenho_ano=empenho_ano,
        empenho_modalidade_nome=empenho_modalidade_nome,
        empenho_modalidade_codigo=empenho_modalidade_codigo,
        empenho_numero=empenho_numero,
        subempenho=subempenho,
        indicador_subempenho=indicador_subempenho,
        credor_codigo=credor_codigo,
        credor_nome=credor_nome,
        modalidade_licitacao_codigo=modalidade_licitacao_codigo,
        modalidade_licitacao_nome=modalidade_licitacao_nome,
        valor_empenhado=valor_empenhado,
        valor_liquidado=valor_liquidado,
        valor_pago=valor_pago
    )

# Teste para o modelo Gasto
@pytest.mark.django_db
def test_gasto_model():

    gasto = create_gasto()

    assert gasto.ano_movimentacao == 2023
    assert gasto.mes_movimentacao == 1
    assert gasto.orgao_codigo == 123
    assert gasto.orgao_nome == 'Ministério da Saúde'
    assert gasto.unidade_codigo == 456
    assert gasto.unidade_nome == 'Unidade de Saúde'
    assert gasto.categoria_economica_codigo == 789
    assert gasto.categoria_economica_nome == 'Categoria Econômica'
    assert gasto.grupo_despesa_codigo == 1011
    assert gasto.grupo_despesa_nome == 'Grupo Despesa'
    assert gasto.modalidade_aplicacao_codigo == 1213
    assert gasto.modalidade_aplicacao_nome == 'Modalidade Aplicação'
    assert gasto.elemento_codigo == 1415
    assert gasto.elemento_nome == 'Elemento'
    assert gasto.subelemento_codigo == 1617
    assert gasto.subelemento_nome == 'Subelemento'
    assert gasto.funcao_codigo == 1819
    assert gasto.funcao_nome == 'Função'
    assert gasto.subfuncao_codigo == 2021
    assert gasto.subfuncao_nome == 'Subfunção'
    assert gasto.programa_codigo == 2223
    assert gasto.programa_nome == 'Programa'
    assert gasto.acao_codigo == 2425
    assert gasto.acao_nome == 'Ação'
    assert gasto.fonte_recurso_codigo == 2627
    assert gasto.fonte_recurso_nome == 'Fonte Recurso'
    assert gasto.empenho_ano == 2023
    assert gasto.empenho_modalidade_nome == 'Modalidade'
    assert gasto.empenho_modalidade_codigo == 2829
    assert gasto.empenho_numero == 3031
    assert gasto.subempenho == 1234.56
    assert gasto.indicador_subempenho == 'Indicador'
    assert gasto.credor_codigo == 3233
    assert gasto.credor_nome == 'Credor'
    assert gasto.modalidade_licitacao_codigo == 3435
    assert gasto.modalidade_licitacao_nome == 'Modalidade Licitação'
    assert gasto.valor_empenhado == 5678.90
    assert gasto.valor_liquidado == 4321.09
    assert gasto.valor_pago == 8765.43
