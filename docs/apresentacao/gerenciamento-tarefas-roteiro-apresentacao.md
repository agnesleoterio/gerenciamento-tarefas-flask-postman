Bo# Roteiro - Apresentação Projeto Portfolio API de Tarefas

**Apresentação: 19:00**

---

## 1. APRESENTAÇÃO PESSOAL (30 segundos)

> "Olá, meu nome é Agnes Leoterio Alves, sou analista de qualidade de software em transição de carreira. Hoje vou apresentar o meu projeto de portfólio, uma API de gerenciamento de tarefas desenvolvida com foco em testes e qualidade desde o início."

---

## 2. O PROJETO EM 2 MINUTOS

### O que é
> "Desenvolvi uma API RESTful para gerenciamento de tarefas usando Python com Flask. É uma API que permite criar, listar, atualizar e excluir tarefas."

### Por que escolhi este projeto
> "Escolhi este projeto porque APIs estão presentes na maioria dos sistemas, e muitas falhas de qualidade acontecem no back-end. Queria demonstrar que sei testar APIs de forma sistemática."

### O problema que resolve
> "Muitas APIs simples não possuem validações adequadas e testes bem definidos, o que gera falhas em operações básicas e dados inconsistentes."

---

## 3. STACK E FERRAMENTAS (1 minuto)

| Ferramenta | Para que serve |
|----------|-----------|
| **Python (Flask)** | Desenvolvimento da API |
| **Postman** | Testes manuais de API |
| **JSON** | Estrutura de dados |
| **HTTP/REST** | Comunicação |

---

## 4. ENDPOINTS TESTADOS (2 minutos)

```
GET    /tasks         → Listar todas as tarefas
POST   /tasks         → Criar nova tarefa
GET    /tasks/<id>   → Buscar tarefa por ID
PUT    /tasks/<id>   → Atualizar tarefa
DELETE /tasks/<id>   → Remover tarefa
POST   /login        → Autenticar usuário
```

### Exemplos de testes

**Cenário positivo - Criar tarefa:**
- Input: `{"title": "teste", "description": "desc", "status": "todo"}`
- Output esperado: `201` + tarefa com ID

**Cenário negativo - Tarefa inexistente:**
- Input: `GET /tasks/999`
- Output esperado: `404` + "task not found"

---

## 5. VALIDAÇÕES IMPLEMENTADAS (1 minuto)

- ✅ Status codes corretos (200, 201, 400, 404)
- ✅ Estrutura e conteúdo do JSON
- ✅ Persistência dos dados após operações
- ✅ Mensagens de erro consistentes

---

## 6. CENÁRIOS DE TESTE (1 minuto)

| Cenário | Tipo |
|--------|------|
| Fluxo positivo (criação e consulta) | Positivo |
| Atualização de dados existentes | Positivo |
| Remoção de registros | Positivo |
| ID inexistente | Negativo |
| Dados inválidos | Negativo |

---

## 7. DESAFIOS E COMO SUPEREI (1 minuto)

**Desafios:**
1. Entendimento da lógica da API
2. Organização eficiente dos testes
3. Validação detalhada das respostas

**Soluções:**
1. Divisão dos testes por endpoint
2. Uso de coleções no Postman
3. Testes incrementais (step-by-step)
4. Revisão de respostas e ajustes contínuos

---

## 8. DIFERENCIAIS (30 segundos)

> "O que diferencia este projeto:
> - Simulação real de testes de API
> - Uso prático de ferramentas do mercado
> - Estrutura pronta para automação futura
> - Mentalidade de QA desde o início do desenvolvimento"

---

## 9. PRÓXIMOS PASSOS (30 segundos)

> "Próximos passos:
> - Automatizar testes com Python (requests/pytest)
> - Integrar com CI/CD
> - Aumentar cobertura de testes
> - Adicionar testes de performance"

---

## 10. CONCLUSÃO (30 segundos)

> "Este projeto consolidou meus conhecimentos em testes de API, me deu experiência prática com Postman, e é a base para evoluir para testes mais avançados com automação."

**Obrigada! Perguntas?**

---

## RESUMO RÁPIDO (para consulta durante apresentação)

| Item | Informação |
|------|-----------|
| **Projeto** | API de Gerenciamento de Tarefas |
| **Stack** | Python (Flask), Postman, JSON, REST |
| **Endpoints** | 6 (GET, POST, PUT, DELETE, /login) |
| **Validações** | Status codes, JSON, persistência, erros |
| **Cenários** | Positivos e negativos |
| **Link** | github.com/agnesleoterio/gerenciamento-tarefas-flask-postman |