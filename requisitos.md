# Requisitos do Projeto - API de Gerenciamento de Tarefas

## 1. Requisitos Funcionais

### 1.1 Gestão de Tarefas

| ID | Requisito | Descrição | Prioridade |
|----|----------|-----------|-----------|
| RF001 | Criar tarefa | O sistema deve permitir criar uma tarefa com título e, opcionalmente, descrição, status, data, prioridade e utilizador | Alta |
| RF002 | Listar tarefas | O sistema deve listar todas as tarefas existentes | Alta |
| RF003 | Buscar tarefa por ID | O sistema deve permitir buscar uma tarefa específica pelo seu ID | Alta |
| RF004 | Atualizar tarefa | O sistema deve permitir atualizar os dados de uma tarefa existente | Alta |
| RF005 | Deletar tarefa | O sistema deve permitir remover uma tarefa existente | Alta |
| RF008 | Filtrar tarefas | O sistema deve permitir filtrar tarefas por status, prioridade e utilizador | Média |
| RF009 | Relatórios | O sistema deve contar tarefas por status e por utilizador | Média |

### 1.2 Autenticação

| ID | Requisito | Descrição | Prioridade |
|----|----------|-----------|-----------|
| RF006 | Login válido | O sistema deve autenticar usuários com credenciais válidas | Alta |
| RF007 | Login inválido | O sistema deve rejeitar credenciais incorretas | Alta |

---

## 2. Estrutura de Dados

### 2.1 Tarefa

```json
{
  "id": 1,
  "title": "string",
  "description": "string",
  "status": "to do | in progress | done",
  "due_date": "YYYY-MM-DD",
  "priority": "low | medium | high",
  "user_id": 1
}
```

### 2.2 Usuário

```json
{
  "id": 1,
  "name": "string",
  "email": "string",
  "password": "string"
}
```

---

## 3. Endpoints da API

| Método | Rota | Descrição | Status Code |
|--------|------|-----------|-------------|
| GET | /tasks | Listar todas as tarefas | 200 |
| GET | /tasks?status=&priority=&user_id= | Filtrar tarefas | 200 |
| GET | /tasks/<id> | Buscar tarefa por ID | 200, 404 |
| POST | /tasks | Criar nova tarefa | 201, 400 |
| PUT | /tasks/<id> | Atualizar tarefa | 200, 400, 404 |
| DELETE | /tasks/<id> | Deletar tarefa | 200, 404 |
| POST | /login | Autenticar usuário | 200, 400 |
| GET | /users | Listar utilizadores sem passwords | 200 |
| GET | /reports/tasks-by-status | Contar tarefas por status | 200 |
| GET | /reports/tasks-by-user | Contar tarefas por utilizador | 200 |
| GET | /health | Verificar disponibilidade da API | 200 |

---

## 4. Requisitos Não Funcionais

| ID | Requisito | Descrição |
|----|----------|---------|
| RNF001 | Formato JSON | Todas as respostas devem ser em formato JSON |
| RNF002 | Codificação UTF-8 | A API deve utilizar codificação UTF-8 |
| RNF003 | Portabilidade | Deve funcionar em Python 3.10+ |
| RNF004 | Estrutura REST | Deve seguir os princípios REST |

---

## 5. Validações Esperadas

### 5.1 Entrada de Dados

- Title deve ser obrigatório
- Descrição é opcional
- Status aceita os valores `to do`, `in progress` e `done`
- Prioridade aceita os valores `low`, `medium` e `high`
- `due_date` é opcional; usar o formato ISO `YYYY-MM-DD`
- A validação rigorosa do formato de `due_date` ainda não está implementada

### 5.2 Respostas de Erro

| Cenário | Status Code | Mensagem |
|--------|------------|----------|
| Tarefa não encontrada | 404 | "task not found" |
| Credenciais inválidas | 400 | "wrong credentials" |
| Título ausente | 400 | "title is required" |
| Status inválido | 400 | "status must be: to do, in progress or done" |
| Prioridade inválida | 400 | "priority must be: low, medium or high" |
| Requisição inválida | 400 | Varia conforme erro |

---

## 6. Casos de Teste

### 6.1 Testes Funcionais

| ID | Cenário de Teste |
|----|----------------|
| TC001 | Criar tarefa com dados válidos |
| TC002 | Criar tarefa sem campos obrigatórios |
| TC003 | Listar todas as tarefas |
| TC004 | Buscar tarefa existente |
| TC005 | Buscar tarefa inexistente |
| TC006 | Atualizar tarefa existente |
| TC007 | Atualizar tarefa inexistente |
| TC008 | Deletar tarefa existente |
| TC009 | Deletar tarefa inexistente |
| TC010 | Login com credenciais válidas |
| TC011 | Login com email inválido |
| TC012 | Login com senha errada |

### 6.2 Testes Negativos

| ID | Cenário de Teste |
|----|----------------|
| TN001 | Acessar tarefa com ID inválido |
| TN002 | Atualizar tarefa inexistente |
| TN003 | Deletar tarefa inexistente |
| TN004 | Login com dados vazios |

---

## 7. Critérios de Aceitação

- [x] GET /tasks retorna lista de tarefas com status 200
- [x] POST /tasks cria tarefa e retorna status 201
- [x] GET /tasks/<id> retorna tarefa específica com status 200
- [x] GET /tasks/<id> inválido retorna status 404
- [x] PUT /tasks/<id> atualiza tarefa com status 200
- [x] DELETE /tasks/<id> remove tarefa com status 200
- [x] POST /login com credenciais válidas retorna status 200
- [x] POST /login com credenciais inválidas retorna status 400
- [x] Respostas em formato JSON
- [x] Mensagens de erro consistentes

---

## 8. Stack Técnologica

| Componente | Tecnologia |
|------------|-----------|
| Linguagem | Python 3.10+ |
| Framework | Flask 3.1.0 |
| Testes Manuais | Postman |
| Testes Automatizados | unittest + Flask test client |
| Banco de Dados | SQLite |
| Formato | JSON |
| Protocolo | HTTP/REST |
