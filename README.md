# API de Gerenciamento de Tarefas 📋
Este é um projeto simples desenvolvido com **Flask** para gerenciar tarefas. Ele permite criar, listar, atualizar e excluir tarefas, servindo como uma introdução ao desenvolvimento de APIs REST, testes utilizando **Postman** e validações com **SQL/SQLite**.

## 📌 Sobre/Objetivo do Projeto

Este projeto foi desenvolvido com o objetivo de praticar o desenvolvimento de APIs utilizando Python e Flask, aplicar conceitos de testes com o Postman, validar dados com SQL e gerenciar o ambiente com o Poetry.

Ele representa uma base sólida para quem está começando a criar APIs REST e precisa entender como os métodos HTTP (GET, POST, PUT, DELETE) funcionam em conjunto com um backend simples e um banco de dados relacional.

---

## 🚀 Funcionalidades

- ✅ Criar uma tarefa (`POST /tasks`)
- 📄 Listar todas as tarefas (`GET /tasks`)
- 🔍 Obter detalhes de uma tarefa específica (`GET /tasks/<id>`)
- ✏️ Atualizar uma tarefa (`PUT /tasks/<id>`)
- ❌ Excluir uma tarefa (`DELETE /tasks/<id>`)
- 👤 Listar utilizadores (`GET /users`)
- 📊 Contar tarefas por status (`GET /reports/tasks-by-status`)
- 📊 Contar tarefas por utilizador (`GET /reports/tasks-by-user`)
- 🔎 Filtrar tarefas por query string:
  - `GET /tasks?status=done`
  - `GET /tasks?priority=high`
  - `GET /tasks?user_id=1`
  
---

## Tecnologias Utilizadas 🛠️
- **Python 3.10**.
- **Flask 3.1.0**: É um framework leve e fácil de usar, ideal para criar APIs e pequenas aplicações web. Vamos criar uma API que realiza operações básicas de CRUD em um banco de dados fictício de tarefas.
- **SQLite**: Banco de dados relacional simples, usado para praticar `SELECT`, `WHERE`, `JOIN`, `COUNT`, `GROUP BY`, `INSERT`, `UPDATE` e `DELETE`.
- **Poetry**: É uma ferramenta para gerenciamento de dependências e empacotamento em Python
- **Postman**: É uma ferramenta que tem como objetivo testar serviços RESTful (Web APIs) por meio do envio de requisições HTTP e da análise do seu retorno. Com ele é possível consumir facilmente serviços locais e na internet, enviando dados e efetuando testes sobre as respostas das requisições.

  ---

## 🧠 O que aprendi com este projeto

- Como estruturar e desenvolver uma API REST utilizando Flask
- Como utilizar o Postman para realizar testes em endpoints
- Gerenciar dependências com o Poetry
- Prática com operações CRUD
- Prática com SQL para validação de dados em QA
- Compreensão das boas práticas para rotas e métodos HTTP
- Comparei frameworks como **Flask** e **FastAPI** para entender diferentes abordagens no desenvolvimento de APIs REST

  ---

## 🔧 Melhorias Futuras

- 🔐 Substituir a autenticação demonstrativa por password hashing e tokens
- ✅ Validar o formato de `due_date` como data ISO (`YYYY-MM-DD`)
- 🧪 Ampliar os testes automatizados e a coleção Postman
- 📝 Registrar evidências das execuções manuais
- 🧠 Criar mais exercícios de SQL com joins, filtros e relatórios
- 💡 Avaliar reescrever este projeto usando FastAPI como forma de aprendizado

---

## Como Executar o Projeto 🔧
1. Clone o repositório pra sua máquina:
```bash
$ git clone git@github.com:agnesleoterio/gerenciamento-tarefas-flask-postman.git && cd gerenciamento-tarefas-flask-postman
```
2. Instale as dependências:
```bash
$ poetry install --no-root
```
3. Execute o servidor Flask:
```bash
$ poetry run flask run
```
4. Acesse a aplicação:
http://127.0.0.1:5000/tasks

## Como estudar SQL neste projeto

1. Inicie a API uma vez para criar o banco `tasks.db`.
2. Abra o banco com SQLite:

```bash
$ sqlite3 tasks.db
```

3. Siga os exercícios no ficheiro [`sql_estudo.md`](sql_estudo.md).

Exemplo de validação:

```sql
SELECT id, title, status, priority
FROM tasks
WHERE status = 'done';
```

## CI/CD

Este projeto possui um workflow de CI com GitHub Actions em `.github/workflows/ci.yml`.

O pipeline executa automaticamente em `push` e `pull_request` para a branch `main`:

1. Faz checkout do repositório.
2. Configura Python 3.10.
3. Instala Poetry.
4. Instala as dependências do projeto.
5. Executa testes automatizados da API com `unittest` e Flask `test_client`.
6. Sobe a API localmente e faz um smoke test com `curl` nos endpoints `/health`, `/tasks` e `/login`.

Para executar os testes localmente:

```bash
poetry run python -m unittest discover -s tests -p "test_*.py"
```

## Testes com Postman

Importe `postman_collection.json` no Postman e mantenha a variável `baseUrl` como `http://localhost:5000`.
A coleção cobre CRUD de tarefas, filtros, login, health check, utilizadores e relatórios. Um script comum valida que as respostas são JSON e não retornam erros 5xx.




