# SPVA - Sistema de Postagens de Vagas e Análise de Currículos

## Descrição do Projeto

O SPVA é um sistema de back-end para um portal de empregos, projetado para conectar candidatos a oportunidades de trabalho. A plataforma permite que empresas postem vagas e gerenciem candidaturas, enquanto os candidatos podem procurar vagas, se candidatar e gerenciar seus perfis e currículos. O sistema é construído com Python e FastAPI, seguindo uma arquitetura de microsserviços e utilizando Docker para conteinerização, facilitando a implantação e escalabilidade.

## Funcionalidades

  - **Gerenciamento de Usuários e Autenticação:**
      - Cadastro e autenticação de usuários com diferentes papéis (candidato, administrador, master) via JWT.
      - Proteção de endpoints com base nos papéis dos usuários.
  - **Gerenciamento de Vagas:**
      - Administradores podem criar, ler, atualizar e deletar vagas de emprego (CRUD).
      - As vagas podem ser categorizadas como remotas, presenciais ou híbridas.
  - **Candidaturas:**
      - Candidatos podem se candidatar a vagas.
      - O sistema rastreia o status da candidatura (enviada, em análise, rejeitada, aceita).
  - **Gerenciamento de Currículos:**
      - Candidatos podem fazer upload de seus currículos, que são armazenados de forma segura no Minio.
  - **API RESTful:**
      - Uma API completa para interagir com todos os recursos do sistema.

## Tecnologias Utilizadas

  - **Back-end:** Python, FastAPI
  - **Banco de Dados:** MySQL
  - **Armazenamento de Objetos:** Minio
  - **ORM:** SQLAlchemy
  - **Autenticação:** JWT (JSON Web Tokens)
  - **Conteinerização:** Docker, Docker Compose
  - **Servidor Web:** Uvicorn, Gunicorn

## Como Executar o Projeto

Existem duas maneiras de executar o projeto: utilizando Docker para uma configuração completa e automatizada, ou localmente para desenvolvimento.

### Modo 1: Executando com Docker (Recomendado)

Este modo orquestra todos os serviços necessários (aplicação, banco de dados e armazenamento de objetos) em contêineres.

**Pré-requisitos:**

  - Docker
  - Docker Compose

**Passos:**

1.  **Clonar o repositório:**

    ```bash
    git clone https://github.com/victordantas1/spva-backend.git
    cd spva-backend
    ```

2.  **Configurar variáveis de ambiente:**

      - Crie um arquivo `.env` a partir do template fornecido.
        ```bash
        cp .env.template .env
        ```
      - Revise o arquivo `.env` e ajuste as variáveis se necessário. Os valores padrão são projetados para funcionar com o `docker-compose.yml`.

3.  **Iniciar os serviços:**

    ```bash
    docker-compose up -d --build
    ```

    Este comando irá construir as imagens e iniciar os contêineres para a aplicação, o banco de dados MySQL e o servidor Minio. A API estará acessível em `http://localhost:8000`.

### Modo 2: Executando Localmente (Desenvolvimento)

Este modo é ideal para desenvolvimento e depuração. Requer que você tenha as dependências (Python, MySQL, Minio) instaladas na sua máquina.

**Pré-requisitos:**

  - Python 3.10 ou superior
  - Acesso a uma instância do MySQL e do Minio.

**Passos:**

1.  **Clonar o repositório:**

    ```bash
    git clone https://github.com/victordantas1/spva-backend.git
    cd spva-backend
    ```

2.  **Criar ambiente virtual e instalar dependências:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows: venv\Scripts\activate
    pip install -r requirements.txt
    ```

3.  **Configurar variáveis de ambiente:**

      - Crie o arquivo `.env` a partir do template:
        ```bash
        cp .env.template .env
        ```
      - **Edite o arquivo `.env`** para apontar para suas instâncias locais do MySQL e Minio, ajustando `DATABASE_URL`, `MINIO_ENDPOINT`, etc.

4.  **Executar o script de inicialização:**

      - Para modo de desenvolvimento com hot-reload:
        ```bash
        ./run.sh dev
        ```
      - Para modo de produção:
        ```bash
        ./run.sh prod
        ```

    A API estará acessível em `http://localhost:8000` (ou na porta que você definir no `.env`).

## Estrutura da API

A API é versionada e os endpoints principais estão localizados em `/api/v1/`.

### Endpoints Principais:

  - **Autenticação:**
      - `POST /auth/login`: Autentica um usuário e retorna um token de acesso.
  - **Usuários:**
      - `GET /users`: Retorna uma lista de todos os usuários (requer privilégios de administrador).
      - `GET /users/me`: Retorna os detalhes do usuário autenticado.
      - `POST /users/upload_resume`: Faz o upload do currículo do usuário autenticado.
  - **Vagas:**
      - `GET /jobs`: Retorna uma lista de todas as vagas.
      - `GET /jobs/{job_id}`: Retorna os detalhes de uma vaga específica.
      - `GET /jobs/{job_id}/candidates`: Retorna uma lista de candidatos para uma vaga específica (requer privilégios de administrador).
  - **Candidaturas:**
      - `POST /user_jobs`: Cria uma nova candidatura para uma vaga.

## Esquema do Banco de Dados

O esquema do banco de dados é definido no arquivo `db_compose/create_tables.sql` e inclui as seguintes tabelas principais:

  - `role_user`: Armazena os papéis dos usuários (ex: admin, candidate).
  - `user_app`: Armazena as informações dos usuários.
  - `job`: Contém os detalhes das vagas de emprego.
  - `user_job`: Tabela de associação que representa as candidaturas dos usuários às vagas.
  - `phone_number`: Armazena os números de telefone dos usuários.