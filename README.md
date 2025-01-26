# API de Gerenciamento de Tarefas 📋
Este é um projeto simples desenvolvido com **Flask** para gerenciar tarefas. Ele permite criar, listar, atualizar e excluir tarefas, servindo como uma introdução ao desenvolvimento de APIs REST e testes utilizando **Postman**.

## Funcionalidades  🚀
- Criar uma tarefa (POST /tasks)
- Listar todas as tarefas (GET /tasks)
- Obter detalhes de uma tarefa específica (GET /tasks/:id)
- Atualizar informações de uma tarefa (PUT /tasks/:id)
- Excluir uma tarefa (DELETE /tasks/:id)

## Tecnologias Utilizadas 🛠️
- **Python 3.10**.
- **Flask 3.1.0**: É um framework leve e fácil de usar, ideal para criar APIs e pequenas aplicações web. Vamos criar uma API que realiza operações básicas de CRUD em um banco de dados fictício de tarefas.
- **Poetry**: É uma ferramenta para gerenciamento de dependências e empacotamento em Python
- **Postman**: É uma ferramenta que tem como objetivo testar serviços RESTful (Web APIs) por meio do envio de requisições HTTP e da análise do seu retorno. Com ele é possível consumir facilmente serviços locais e na internet, enviando dados e efetuando testes sobre as respostas das requisições.

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



