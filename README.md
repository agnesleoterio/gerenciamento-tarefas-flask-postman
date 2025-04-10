# API de Gerenciamento de Tarefas 📋
Este é um projeto simples desenvolvido com **Flask** para gerenciar tarefas. Ele permite criar, listar, atualizar e excluir tarefas, servindo como uma introdução ao desenvolvimento de APIs REST e testes utilizando **Postman**.

## 📌 Sobre o Projeto

Este projeto foi desenvolvido com o objetivo de praticar o desenvolvimento de APIs utilizando Python e Flask, além de aplicar conceitos de testes com o Postman e gerenciar o ambiente com o Poetry.

Ele representa uma base sólida para quem está começando a criar APIs REST e precisa entender como os métodos HTTP (GET, POST, PUT, DELETE) funcionam em conjunto com um backend simples.

---

## 🚀 Funcionalidades

- ✅ Criar uma tarefa (`POST /tasks`)
- 📄 Listar todas as tarefas (`GET /tasks`)
- 🔍 Obter detalhes de uma tarefa específica (`GET /tasks/<id>`)
- ✏️ Atualizar uma tarefa (`PUT /tasks/<id>`)
- ❌ Excluir uma tarefa (`DELETE /tasks/<id>`)
  
---

## Tecnologias Utilizadas 🛠️
- **Python 3.10**.
- **Flask 3.1.0**: É um framework leve e fácil de usar, ideal para criar APIs e pequenas aplicações web. Vamos criar uma API que realiza operações básicas de CRUD em um banco de dados fictício de tarefas.
- **Poetry**: É uma ferramenta para gerenciamento de dependências e empacotamento em Python
- **Postman**: É uma ferramenta que tem como objetivo testar serviços RESTful (Web APIs) por meio do envio de requisições HTTP e da análise do seu retorno. Com ele é possível consumir facilmente serviços locais e na internet, enviando dados e efetuando testes sobre as respostas das requisições.

  ---

## 🧠 O que aprendi com este projeto

- Como estruturar e desenvolver uma API REST utilizando Flask
- Como utilizar o Postman para realizar testes em endpoints
- Gerenciar dependências com o Poetry
- Prática com operações CRUD
- Compreensão das boas práticas para rotas e métodos HTTP
- Comparei frameworks como **Flask** e **FastAPI** para entender diferentes abordagens no desenvolvimento de APIs REST

  ---

## 📈 Melhorias Futuras

- 🔐 Implementação de autenticação e autorização (ex.: JWT, OAuth) para testar cenários com diferentes tipos de usuários  
- 🧪 Adição de testes automatizados com **Pytest**, focando em testes de unidade e de integração  
- ⚙️ Integração com **banco de dados real** (SQLite ou PostgreSQL) para testes mais realistas  
- 🧰 Integração com ferramentas de **CI/CD** (como GitHub Actions) para execução automatizada de testes  
- 📊 Geração de relatórios de testes com **Allure** ou ferramentas similares  
- 📦 Criação de massa de dados usando **Faker** para testes automatizados mais robustos  
- 📁 Organização de cenários de teste e planejamento com ferramentas como **TestRail** ou **Xray**
- 🔁 Reescrever ou adaptar o projeto com **FastAPI**, explorando recursos modernos como documentação automática com Swagger UI

---

## Como Executar o Projeto 🔧
1. Clone o repositório pra sua máquina:
```bash
$ git clone git@github.com:agnesleoterio/gerenciamento-tarefas-flask-postman.git && cd gerenciamento-tarefas-flask-postman
```
2. Instale as dependências do projeto. Caso queira usar o Poetry, [aqui segue um guia](https://www.alura.com.br/artigos/ven-poetry-no-python).
3. Execute o servidor Flask:
```bash
$ flask run
```
4. Acesse a aplicação:
http://127.0.0.1:5000/tasks



