
# Projeto de Gastos Públicos

Este é um projeto Django para rastreamento e gerenciamento de gastos públicos. Ele fornece uma interface para visualizar, adicionar, editar e excluir dados relacionados aos gastos públicos, além de uma api rest para outros desenvolvedores.

## Pré-requisitos

- Python 3.10
- Virtualenv (opcional, mas recomendado)
- PostgreSQL (ou outro banco de dados compatível com Django)

## Configuração do Ambiente


1 **Clone este repositório:**
    
```bash
git clone https://github.com/lucasribeirorsousa/projeto-gastos.git
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

## Inicialização do Servidor
Para iniciar o servidor de desenvolvimento do Django, execute o seguinte comando:
```bash 
python manage.py runserver
```
Isso iniciará o servidor em http://localhost:8000/. Você pode acessar a interface do projeto a partir desse endereço.
