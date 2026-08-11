# Plano de Testes - API de Gerenciamento de Tarefas

Ambiente automatizado: Flask `test_client` com uma base SQLite temporária criada para cada teste.

| ID | Cenário | Endpoint | Método | Dados de Entrada | Resultado Esperado | Automação | Status |
|----|---------|----------|--------|------------------|-------------------|-----------|--------|
| TC001 | Health check | `/health` | GET | N/A | 200 + `status: ok` | `test_health_check_returns_ok` | Passou |
| TC002 | Login válido | `/login` | POST | Email e password válidos | 200 + utilizador sem password | `test_login_with_valid_credentials` | Passou |
| TC003 | Login inválido | `/login` | POST | Password incorreta | 400 + `wrong credentials` | `test_login_with_wrong_credentials_returns_400` | Passou |
| TC004 | Login incompleto | `/login` | POST | Sem password | 400 + mensagem de campos obrigatórios | `test_login_without_password_returns_400` | Passou |
| TC005 | Listar e buscar tarefa existente | `/tasks`, `/tasks/<id>` | GET | N/A | 200 + dados da tarefa | `test_list_and_get_existing_task` | Passou |
| TC006 | Buscar tarefa inexistente | `/tasks/999` | GET | N/A | 404 + `task not found` | `test_get_missing_task_returns_404` | Passou |
| TC007 | Criar tarefa válida | `/tasks` | POST | `title`, `description`, `status`, `priority`, `user_id` | 201 + tarefa com ID | `test_create_task_with_valid_payload` | Passou |
| TC008 | Criar tarefa sem título | `/tasks` | POST | Sem `title` | 400 + `title is required` | `test_create_task_without_title_returns_400` | Passou |
| TC009 | Criar tarefa com status inválido | `/tasks` | POST | `status: todo` | 400 + valores permitidos | `test_create_task_with_invalid_status_returns_400` | Passou |
| TC010 | Filtrar por status | `/tasks?status=done` | GET | N/A | 200 + apenas tarefas concluídas | `test_filter_tasks_by_status` | Passou |
| TC011 | Atualizar e eliminar tarefa | `/tasks/<id>` | PUT/DELETE | Status e prioridade válidos | 200 nas duas operações; depois 404 | `test_update_and_delete_task` | Passou |
| TC012 | Relatório por status | `/reports/tasks-by-status` | GET | N/A | 200 + totais agrupados | `test_reports_tasks_by_status` | Passou |
| TC013 | Relatório por utilizador | `/reports/tasks-by-user` | GET | N/A | 200 + totais por utilizador | `test_reports_tasks_by_user` | Passou |
| TC014 | Listar utilizadores com segurança | `/users` | GET | N/A | 200 sem expor passwords | `test_users_response_does_not_expose_passwords` | Passou |

## Cenários manuais pendentes

- Confirmar filtros combinados por status, prioridade e utilizador.
- Confirmar persistência dos dados após reiniciar a aplicação.
- Confirmar o workflow Docker de ponta a ponta.
- Validar a coleção Postman num ambiente local em execução.
- Registrar evidências das execuções manuais.
