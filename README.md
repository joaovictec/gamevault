# GameVault API

API REST para gerenciamento de estoque e revenda de videogames.

O projeto foi desenvolvido com Python e FastAPI, utilizando SQLite para persistência dos dados e Pytest para testes automatizados.

## Tecnologias

- Python 3.12+
- FastAPI
- SQLAlchemy
- SQLite
- Pydantic
- Pytest
- GitHub Actions
- Git Flow

##  Funcionalidades

- Cadastro de jogos
- Listagem de jogos
- Busca de jogo por ID
- Atualização de jogos
- Exclusão de jogos
- Filtros por plataforma
- Filtros por faixa de preço
- Dashboard do estoque
- Registro de vendas
- Controle de status dos jogos
- Testes automatizados
- Integração contínua com GitHub Actions

##  Endpoints

### Jogos

| Método | Endpoint | Descrição |
|---|---|---|
| POST | `/games/` | Cadastrar jogo |
| GET | `/games/` | Listar jogos |
| GET | `/games/{id}` | Buscar jogo |
| PUT | `/games/{id}` | Atualizar jogo |
| DELETE | `/games/{id}` | Excluir jogo |
| POST | `/games/{id}/sell` | Registrar venda |
| GET | `/games/dashboard/summary` | Resumo do estoque |

### Filtros

Exemplos:

```text
GET /games/?platform=PS5
GET /games/?min_price=100
GET /games/?max_price=200
Os filtros podem ser combinados:
GET /games/?platform=PS5&min_price=100&max_price=300
▶️ Como executar
1. Clone o projeto
git clone URL_DO_REPOSITORIO
cd gamevault
2. Crie o ambiente virtual
python -m venv .venv
3. Ative o ambiente virtual
No Windows PowerShell:
.venv\Scripts\Activate.ps1
4. Instale as dependências
pip install -r requirements.txt
5. Execute a API
python -m uvicorn app.main:app --reload
A API estará disponível em:
http://127.0.0.1:8000
📚 Documentação da API
O FastAPI fornece documentação interativa automaticamente.
Swagger UI:
http://127.0.0.1:8000/docs
ReDoc:
http://127.0.0.1:8000/redoc
🧪 Testes
O projeto utiliza Pytest para testes automatizados.
Para executar os testes:
pytest -v
Os testes verificam funcionalidades como:
Inicialização da API
Cadastro de jogos
Listagem
Dashboard
Filtros
Atualização de jogos
Registro de vendas
Prevenção de venda duplicada
🔄 Integração Contínua
O projeto utiliza GitHub Actions para executar automaticamente os testes.
O workflow é executado em alterações nas branches:
main
develop
O processo de CI realiza:
Checkout do código
Configuração do Python
Instalação das dependências
Execução dos testes com Pytest
🌿 Git Flow
O desenvolvimento utiliza Git Flow para organização das branches.
Estrutura principal:
main
  │
  └── develop
       │
       └── feature/*
As novas funcionalidades são desenvolvidas em branches específicas:
feature/nome-da-feature
Após a conclusão, a feature é integrada ao develop.
Antes da versão final, será criada uma branch de release:
release/1.0.0
Após a validação, a versão será integrada ao main e receberá a tag:
v1.0.0
🗂️ Estrutura do Projeto
gamevault/
├── app/
│ ├── main.py
│ ├── database.py
│ │
│ ├── models/
│ │ └── game.py
│ │
│ ├── schemas/
│ │ └── game.py
│ │
│ ├── routes/
│ │ └── games.py
│ │
│ └── services/
│ └── game_service.py
│
├── tests/
│ └── test_games.py
│
├── .github/
│ └── workflows/
│ └── tests.yml
│
├── .gitignore
├── requirements.txt
└── README.md
🎯 Objetivo
O GameVault foi desenvolvido como projeto de portfólio para demonstrar conhecimentos em:
Desenvolvimento de APIs REST
Python
FastAPI
Banco de dados
SQLAlchemy
ORM
Pydantic
Validação de dados
Testes automatizados
Git
Git Flow
Integração contínua
🔮 Próximos passos
Possíveis evoluções futuras:
Autenticação de usuários
Controle de clientes
Histórico de vendas
Relatórios financeiros
Controle de lucro por venda
Paginação
Banco de dados PostgreSQL
Docker
Deploy em ambiente cloud
📄 Licença
Este projeto está sob a licença MIT.

### ⚠️ Uma coisa importante

Onde está:

```text
URL_DO_REPOSITORIO