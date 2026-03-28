# Book Scraper — Fullstack

Aplicação fullstack para coleta, armazenamento e visualização de livros via web scraping.

O backend realiza o scraping, persiste os dados em banco relacional e os expõe via API REST. O frontend consome essa API e exibe os livros em uma interface web.

---

## Stack

| Camada | Tecnologia |
|---|---|
| Backend | Python · FastAPI · SQLAlchemy |
| Scraping | httpx · BeautifulSoup4 |
| Banco de dados | MySQL |
| Frontend | React · TypeScript · Vite |
| Validação | Pydantic |
| Testes | pytest · pytest-cov |
| Gerenciador de pacotes | Poetry |

---

## Estrutura do projeto

```
book-scraper/
├── app/
│   ├── api/
│   │   └── books_router.py         # Rotas FastAPI
│   ├── db/
│   │   ├── base.py                 # Base declarativa do SQLAlchemy
│   │   └── session.py              # Configuração da sessão com o banco
│   ├── models/
│   │   ├── book.py                 # Modelo ORM da tabela books
│   │   └── category.py             # Modelo ORM da tabela categories
│   ├── repositories/
│   │   └── book_repository.py      # Queries ao banco de dados
│   ├── schemas/
│   │   └── book.py                 # Schemas Pydantic (request/response)
│   ├── scraper/
│   │   ├── books_scraper.py        # Orquestra o scraping
│   │   └── parser.py               # Extrai dados do HTML
│   ├── services/
│   │   └── bookservice.py          # Lógica de negócio
│   ├── settings/
│   │   └── db_config.py            # Variáveis de configuração do banco
│   └── main.py                     # Ponto de entrada da aplicação
│
├── tests/
│   ├── test_parser.py              # Testes do parser de scraping
│   └── test_routes.py              # Testes dos endpoints da API
│
├── frontend/
│   └── src/
│       ├── components/
│       │   ├── BookCard.tsx         # Exibe um livro individual
│       │   └── BookListFecth.tsx    # Busca e lista os livros
│       ├── services/
│       │   └── api.ts               # Comunicação com o backend
│       ├── styles/
│       │   ├── globalStyles.ts
│       │   ├── AppStyle.ts
│       │   ├── BookCardStyle.tsx
│       │   └── BookListStyle.ts
│       ├── types/
│       │   └── book.ts              # Interfaces TypeScript
│       ├── assets/
│       │   └── hero.png
│       ├── App.tsx
│       └── main.tsx
│
├── pyproject.toml
└── poetry.lock
```

---

## Pré-requisitos

- [Python 3.14+](https://www.python.org/)
- [Node.js 18+](https://nodejs.org/)
- [MySQL 8+](https://dev.mysql.com/downloads/)
- [Poetry](https://python-poetry.org/) — gerenciador de dependências do backend

---

## Instalação e execução

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/book-scraper.git
cd book-scraper
```

### 2. Configure o banco de dados

Crie o banco no MySQL:

```sql
CREATE DATABASE book_scraper CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

### 3. Backend

Instale as dependências:

```bash
poetry install
```

Configure as variáveis de ambiente em `app/settings/db_config.py` ou via `.env`:

```env
DATABASE_URL=mysql+pymysql://usuario:senha@localhost:3306/book_scraper
```

Inicie o servidor:

```bash
poetry run uvicorn app.main:app --reload
```

A API estará disponível em `http://127.0.0.1:8000`.  
A documentação interativa (Swagger) fica em `http://127.0.0.1:8000/docs`.

### 4. Frontend

```bash
cd frontend
npm install
npm run dev
```

A interface estará disponível em `http://localhost:5173`.

---

## Endpoints

Base URL: `http://127.0.0.1:8000`

| Método | Endpoint | Descrição |
|---|---|---|
| `GET` | `/api/books/` | Lista todos os livros |
| `GET` | `/api/books/{id}` | Retorna um livro pelo ID |

### Exemplo de resposta — `GET /api/books/`

```json
[
  {
    "id": 1,
    "title": "A Light in the Attic",
    "price": "£51.77",
    "rating": "Three",
    "availability": "In stock"
  }
]
```

### Paginação

```
GET /api/books/?skip=0&limit=20
```

| Parâmetro | Tipo | Padrão | Descrição |
|---|---|---|---|
| `skip` | int | 0 | Registros a pular |
| `limit` | int | 20 | Registros a retornar |

---

## Arquitetura do backend

O backend segue uma separação em camadas:

```
Request -> Router -> Service -> Repository -> Database
                       |
                    Scraper (httpx + BeautifulSoup)
```

- **Router** (`api/books_router.py`) — recebe as requisições HTTP e delega ao service
- **Service** (`services/bookservice.py`) — contém a lógica de negócio
- **Repository** (`repositories/book_repository.py`) — isola as queries ao banco
- **Scraper** (`scraper/`) — `books_scraper.py` orquestra a coleta e `parser.py` extrai os dados do HTML
- **Models** (`models/`) — mapeamento ORM com SQLAlchemy
- **Schemas** (`schemas/`) — validação e serialização com Pydantic

---

## Modelo de dados

### Tabela `books`

| Coluna | Tipo | Descrição |
|---|---|---|
| `id` | INT (PK) | Identificador único |
| `title` | VARCHAR | Título do livro |
| `price` | VARCHAR | Preço com símbolo (ex: `£51.77`) |
| `rating` | VARCHAR | Avaliação textual (ex: `Three`) |
| `availability` | VARCHAR | Disponibilidade (ex: `In stock`) |

### Tabela `categories`

| Coluna | Tipo | Descrição |
|---|---|---|
| `id` | INT (PK) | Identificador único |
| `name` | VARCHAR | Nome da categoria |

---

## CORS

O backend aceita requisições das seguintes origens:

```
http://localhost:5173
http://localhost:3000
```

Para alterar, edite o middleware em `app/main.py`.

---

## Testes

```bash
# Roda todos os testes
poetry run pytest

# Com relatório de cobertura
poetry run pytest --cov=app tests/
```

Os testes estão organizados em:

- `tests/test_parser.py` — testa a extração de dados do HTML pelo parser
- `tests/test_routes.py` — testa os endpoints da API

---

## Scripts disponíveis

### Backend

```bash
poetry run uvicorn app.main:app --reload   # Inicia o servidor
poetry run pytest                          # Roda os testes
```

### Frontend

```bash
npm run dev        # Inicia o servidor de desenvolvimento
```

---


