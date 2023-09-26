
# Projeto de Gastos Públicos

Este é um projeto Django para rastreamento e gerenciamento de gastos públicos. Ele fornece uma interface para visualizar, adicionar, editar e excluir dados relacionados aos gastos públicos, além de uma api rest para outros desenvolvedores.

## Pré-requisitos

- Python 3.10
- Virtualenv (opcional, mas recomendado)
- PostgreSQL (ou outro banco de dados compatível com Django)

## Configuração do Ambiente


1 **Clone este repositório:**
    
```bash
git clone https://github.com/seu-usuario/projeto-gastos.git
cd projeto-gastos
```

2 **Crie um ambiente virtual (opcional, mas recomendado):**
```bash
python -m venv venv
source venv/bin/activate  # No Windows, use 'venv\Scripts\activate'
```

3 **Instale as dependências do projeto:**
```bash
pip install -r requirements.txt
```

4 **Crie um super usuário:**
```bash
python manage.py createsuperuser
```

## Configuração do Banco de Dados

1 **Certifique-se de que você tenha um banco de dados PostgreSQL instalado e configurado.**

2 **Crie um banco de dados para o projeto e defina as credenciais no arquivo .env. Você pode copiar o arquivo .env.example e renomeá-lo para .env, ajustando as configurações conforme necessário:**
```bash
# .env

# Configurações do Banco de Dados
DB_ENGINE=django.db.backends.postgresql
DB_NAME=nyx
DB_USER=seu-usuario
DB_PASSWORD=sua-senha
DB_HOST=localhost
DB_PORT=5432
```

3 **Execute as migrações do Django para criar as tabelas do banco de dados:**
```bash 
python manage.py migrate
```

3 **Carregue dados de exemplo:**
```bash 
python manage.py loaddata fixtures/gastos_fixture.json
```

## Inicialização do Servidor
Para iniciar o servidor de desenvolvimento do Django, execute o seguinte comando:
```bash 
python manage.py runserver
```
Isso iniciará o servidor em http://localhost:8000/. Você pode acessar a interface do projeto a partir desse endereço.


## Rotas
Aqui estão as principais rotas do projeto:

- Página principal: http://localhost:8000/
- Página de administração: http://localhost:8000/admin/
- Visualizar gastos por mês: http://localhost:8000/despesas_por_mes/
- Visualizar gastos por categoria: http://localhost:8000/despesas_por_categoria/
- Visualizar fontes de dinheiro: http://localhost:8000/fontes_de_dinheiro/
- Visualizar todos os dados: http://localhost:8000/todos_os_dados/
- Adicionar/Editar Dados: http://localhost:8000/adicionar_editar_dados/
- Editar Dados (ID específico): http://localhost:8000/editar_dados/1/ (substitua "1" pelo ID desejado)
- Excluir Dados (ID específico): http://localhost:8000/excluir_dados/1/ (substitua "1" pelo ID desejado)

API:
- API para todos os dados: http://localhost:8000/api/todos_os_dados/
- API para detalhes de um dado específico (ID específico): http://localhost:8000/api/todos_os_dados/1/ (substitua "1" pelo ID desejado)