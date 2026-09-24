# 🎮 GameVault API

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.12+-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python 3.12+">
  <img src="https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi" alt="FastAPI">
  <img src="https://img.shields.io/badge/SQLAlchemy-D71F0E?style=for-the-badge&logo=sqlalchemy&logoColor=white" alt="SQLAlchemy">
  <img src="https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white" alt="SQLite">
  <img src="https://img.shields.io/badge/Pytest-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white" alt="Pytest">
  <img src="https://img.shields.io/badge/GitHub_Actions-2088FF?style=for-the-badge&logo=github-actions&logoColor=white" alt="GitHub Actions">
  <img src="https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge" alt="License MIT">
</p>

<p align="center">
  <b>API RESTful para gerenciamento completo de estoque e controle de revenda de videogames.</b>
</p>

---

## 📌 Sobre o Projeto

O **GameVault API** foi desenvolvido com o propósito de demonstrar boas práticas na construção de serviços backend modernos utilizando o ecossistema Python. Ele resolve problemas comuns de controle de estoque de jogos, gerenciando status do catálogo, vendas e relatórios simplificados.

### 🎯 Objetivos Demonstrados
* Arquitetura limpa com separação de responsabilidades (Rotas, Serviços, Schemas e Modelos).
* Validação rigorosa de dados com **Pydantic**.
* ORM robusto utilizando **SQLAlchemy**.
* Testes automatizados cobrindo fluxos principais e exceções de regra de negócio.
* Integração Contínua (CI) e controle rigoroso de fluxo de trabalho Git (**Git Flow**).

---


## ⚙️ Tecnologias Utilizadas

- **Linguagem:** Python 3.12+
- **Framework Web:** FastAPI
- **Validação de Dados:** Pydantic
- **Persistência / ORM:** SQLAlchemy & SQLite
- **Testes Automáticos:** Pytest
- **CI/CD:** GitHub Actions
- **Controle de Versão:** Git & Git Flow

---

## ✨ Funcionalidades

- [x] **Gestão de Catálogo:** Cadastro, listagem, consulta por ID, atualização e exclusão de jogos.
- [x] **Filtros Avançados:** Filtre o estoque simultaneamente por plataforma e faixa de preço (`min_price` / `max_price`).
- [x] **Controle de Vendas:** Registro de vendas com alteração imediata do status e proteção contra vendas duplicadas.
- [x] **Dashboard do Estoque:** Métricas sumarizadas e indicadores em tempo real.
- [x] **Qualidade Continua:** Suite de testes integrados ao pipeline do GitHub Actions.

---

## 🛠️ Endpoints da API

### 🕹️ Jogos

| Método | Endpoint | Descrição | Status Code |
| :---: | :--- | :--- | :---: |
| `POST` | `/games/` | Cadastrar novo jogo no estoque | `201` |
| `GET` | `/games/` | Listar todos os jogos (com suporte a filtros) | `200` |
| `GET` | `/games/{id}` | Buscar detalhes de um jogo específico | `200` |
| `PUT` | `/games/{id}` | Atualizar informações de um jogo | `200` |
| `DELETE` | `/games/{id}` | Remover jogo do banco de dados | `200` |
| `POST` | `/games/{id}/sell` | Registrar venda de um jogo | `200` |
| `GET` | `/games/dashboard/summary` | Obter resumo estatístico do estoque | `200` |
<img width="598" height="282" alt="Captura de tela 2026-09-24 115808" src="https://github.com/user-attachments/assets/4bdf1622-7d6c-40f2-bd88-7bb8a441d7bc" />
<img width="598" height="282" alt="Captura de tela 2026-09-24 115757" src="https://github.com/user-attachments/assets/77be1039-436b-4e66-a11a-d95a8f3c4df6" />

### 🔍 Filtros de Busca

Os parâmetros de busca podem ser utilizados individualmente ou combinados na query string:

```http
GET /games/?platform=PS5
GET /games/?min_price=100
GET /games/?max_price=200
GET /games/?platform=PS5&min_price=100&max_price=300
🚀 Como Executar o Projeto
Pré-requisitos
Python 3.12 ou superior instalado.

Git instalado.

Passo a Passo
Clonar o repositório:

Bash
git clone [https://github.com/SEU_USUARIO/gamevault.git](https://github.com/SEU_USUARIO/gamevault.git)
cd gamevault
Criar e ativar o ambiente virtual:

Windows (PowerShell):

PowerShell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
Linux / macOS:

Bash
python3 -m venv .venv
source .venv/bin/activate
Instalar as dependências:

Bash
pip install --upgrade pip
pip install -r requirements.txt
Iniciar o servidor da API:

Bash
python -m uvicorn app.main:app --reload
Acessar a aplicação:
A API estará rodando em: http://127.0.0.1:8000

📚 Documentação Interativa
Com o servidor rodando, você pode explorar e testar a API através da documentação OpenAPI gerada automaticamente:

Swagger UI: http://127.0.0.1:8000/docs

ReDoc: http://127.0.0.1:8000/redoc

🧪 Executando os Testes
Para garantir a qualidade e a integridade da aplicação, utilize o Pytest:

Bash
pytest -v
Os testes automatizados cobrem:

[x] Inicialização e conectividade da API

[x] Regras de criação, listagem, atualização e remoção

[x] Aplicação dos filtros de consulta

[x] Lógica do dashboard do estoque

[x] Regra de negócio: Prevenção contra venda duplicada de jogos

🔄 Integração Contínua (CI)
O projeto possui integração com o GitHub Actions (.github/workflows/tests.yml), executando a suíte de testes automaticamente a cada push ou pull_request enviado para as branches:

main

develop

🌿 Estrutura de Branches (Git Flow)
Seguimos a convenção de ramificação Git Flow para o ciclo de vida do desenvolvimento:

Plaintext
main
 │
 └── develop
       │
       └── feature/nome-da-feature
main: Código estável em produção.

develop: Branch principal de integração.

feature/*: Desenvolvimento de novas funcionalidades.

release/*: Preparação de versões para homologação e criação de tags (v1.0.0).

🗂️ Estrutura do Projeto
Plaintext
gamevault/
├── .github/
│   └── workflows/
│       └── tests.yml      # Workflow de Integração Contínua (CI)
├── app/
│   ├── models/            # Modelos do banco de dados (SQLAlchemy)
│   │   └── game.py
│   ├── routes/            # Controladores / Endpoints
│   │   └── games.py
│   ├── schemas/           # Validações e Serializadores (Pydantic)
│   │   └── game.py
│   ├── services/          # Camada de Regras de Negócio
│   │   └── game_service.py
│   ├── database.py        # Conexão e sessão do banco de dados
│   └── main.py            # Ponto de entrada da aplicação FastAPI
├── tests/
│   └── test_games.py      # Testes de integração e unidade
├── .gitignore
├── requirements.txt
└── README.md
🔮 Roadmap / Próximos Passos
[ ] Implementação de Autenticação e Autorização (OAuth2 / JWT)

[ ] Cadastro e gestão de clientes

[ ] Relatórios financeiros com margem de lucro por venda

[ ] Paginação e ordenação nos endpoints de listagem

[ ] Suporte a PostgreSQL via variáveis de ambiente

[ ] Containerização da aplicação com Docker e Docker Compose

[ ] Deploy automatizado em nuvem (Render, Railway ou AWS)

📄 Licença
Este projeto está distribuído sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

💡 Dicas importantes antes de salvar:
Subsitua SEU_USUARIO no link do git clone e no rodapé pelo seu username do GitHub.

Certifique-se de alterar as URLs dos badges ou imagens caso altere os nomes das tecnologias no futuro.
