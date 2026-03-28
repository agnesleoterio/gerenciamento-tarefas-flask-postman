# Plano de Testes - API Gerenciamento de Tarefas

| ID | Cenário | Endpoint | Método | Dados de Entrada | Resultado Esperado | Resultado Real | Status | Ambiente |
|----|---------|----------|--------|------------------|-------------------|----------------|--------|----------|
| TC001 | Login com credenciais válidas | `/login` | POST | `{"email": "ana@example.com", "password": "123456"}` | 200 + message "login successful" | | | Dev |
| TC002 | Login com email inválido | `/login` | POST | `{"email": "errado@example.com", "password": "123456"}` | 400 + message "wrong credentials" | | | Dev |
| TC003 | Login com senha errada | `/login` | POST | `{"email": "ana@example.com", "password": "errado"}` | 400 + message "wrong credentials" | | | Dev |
| TC004 | Login com dados incompletos | `/login` | POST | `{"email": "ana@example.com"}` | 400 ou erro | | | Dev |
| TC005 | Listar todas as tarefas | `/tasks` | GET | N/A | 200 + lista de tarefas | | | Dev |
| TC006 | Buscar tarefa existente | `/tasks/1` | GET | N/A | 200 + dados da tarefa | | | Dev |
| TC007 | Buscar tarefa inexistente | `/tasks/999` | GET | N/A | 404 + "task not found" | | | Dev |
| TC008 | Criar tarefa com dados válidos | `/tasks` | POST | `{"title": "teste", "description": "desc", "status": "todo", "date": "01/01/2025"}` | 201 + tarefa com ID | | | Dev |
| TC009 | Criar tarefa sem campos obrigatórios | `/tasks` | POST | `{"title": "teste"}` | 201 ou 400 | | | Dev |
| TC010 | Atualizar tarefa existente | `/tasks/1` | PUT | `{"status": "done"}` | 200 + tarefa atualizada | | | Dev |
| TC011 | Atualizar tarefa inexistente | `/tasks/999` | PUT | `{"status": "done"}` | 404 + "task not found" | | | Dev |
| TC012 | Deletar tarefa existente | `/tasks/1` | DELETE | N/A | 200 + "task deleted" | | | Dev |
| TC013 | Deletar tarefa inexistente | `/tasks/999` | DELETE | N/A | 404 + "task not found" | | | Dev |
