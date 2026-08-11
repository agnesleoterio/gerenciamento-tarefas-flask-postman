# Guia de Estudo SQL com a API de Tarefas

Este projeto agora usa SQLite. O banco fica no ficheiro `tasks.db`, criado automaticamente quando a API inicia.

## Como abrir o banco

Na pasta do projeto:

```bash
sqlite3 tasks.db
```

Dentro do SQLite, alguns comandos úteis:

```sql
.tables
.schema tasks
.schema users
.headers on
.mode column
```

## Estrutura principal

Tabelas:

- `users`: utilizadores
- `tasks`: tarefas

Relação:

- `tasks.user_id` aponta para `users.id`

## Queries essenciais

### 1. Ver todas as tarefas

```sql
SELECT *
FROM tasks;
```

### 2. Ver campos específicos

```sql
SELECT id, title, status, priority
FROM tasks;
```

### 3. Filtrar por status

```sql
SELECT id, title, status
FROM tasks
WHERE status = 'done';
```

### 4. Filtrar por prioridade

```sql
SELECT id, title, priority
FROM tasks
WHERE priority = 'high';
```

### 5. Contar tarefas

```sql
SELECT COUNT(*) AS total_tasks
FROM tasks;
```

### 6. Contar tarefas por status

```sql
SELECT status, COUNT(*) AS total
FROM tasks
GROUP BY status;
```

### 7. Juntar tarefas com utilizadores

```sql
SELECT
    tasks.id,
    tasks.title,
    tasks.status,
    users.name AS user_name
FROM tasks
LEFT JOIN users ON users.id = tasks.user_id;
```

### 8. Ver tarefas de uma utilizadora

```sql
SELECT
    tasks.id,
    tasks.title,
    tasks.status,
    users.name AS user_name
FROM tasks
INNER JOIN users ON users.id = tasks.user_id
WHERE users.email = 'ana@example.com';
```

### 9. Validar uma tarefa criada pela API

Depois de fazer `POST /tasks`, usa o `id` retornado:

```sql
SELECT *
FROM tasks
WHERE id = 4;
```

### 10. Validar uma atualização feita pela API

Depois de fazer `PUT /tasks/4`:

```sql
SELECT id, title, status, priority, updated_at
FROM tasks
WHERE id = 4;
```

### 11. Procurar texto no título

```sql
SELECT id, title, status
FROM tasks
WHERE title LIKE '%SQL%';
```

### 12. Ordenar por data

```sql
SELECT id, title, due_date, priority
FROM tasks
ORDER BY due_date ASC;
```

## Exercícios para QA

1. Criar uma tarefa pela API e confirmar no banco com `SELECT`.
2. Atualizar o `status` de uma tarefa pela API e confirmar no banco.
3. Filtrar `GET /tasks?status=done` e comparar com:

```sql
SELECT *
FROM tasks
WHERE status = 'done';
```

4. Comparar `GET /reports/tasks-by-status` com:

```sql
SELECT status, COUNT(*) AS total
FROM tasks
GROUP BY status
ORDER BY total DESC;
```

5. Comparar `GET /reports/tasks-by-user` com:

```sql
SELECT
    users.id AS user_id,
    users.name AS user_name,
    COUNT(tasks.id) AS total_tasks
FROM users
LEFT JOIN tasks ON tasks.user_id = users.id
GROUP BY users.id, users.name
ORDER BY total_tasks DESC;
```

## Frase para entrevista

Uso SQL em QA para validar se os dados criados ou alterados pela API foram gravados corretamente no banco, comparar respostas da API com a base de dados e apoiar investigação de bugs.
