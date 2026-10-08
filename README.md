# Orbe

Aplicativo mobile de controle financeiro pessoal.

> **Ver. Entender. Decidir.**

O Orbe tem como objetivo permitir que o usuário registre receitas e despesas, organize seus lançamentos por categoria e visualize sua situação financeira em um dashboard.

## Status

**MVP em desenvolvimento — escopo congelado**

Prazo de desenvolvimento: **4 semanas**.

---

## Produto

O Orbe é um aplicativo de controle financeiro pessoal focado em:

- registrar receitas;
- registrar despesas;
- categorizar movimentações;
- visualizar receitas e gastos de um período;
- calcular o resultado do mês;
- acompanhar o comprometimento da renda;
- visualizar a distribuição das despesas por categoria;
- consultar o histórico de lançamentos.

O fluxo principal do MVP é:

```text
Cadastro
   ↓
Login
   ↓
Dashboard
   ↓
Novo lançamento
   ↓
Receita / Despesa
   ↓
Persistência
   ↓
Dashboard atualizado
   ↓
Histórico
```

---

## Escopo do MVP

### 🔴 Obrigatório

### Autenticação

- [ ] Cadastro
- [ ] Login
- [ ] Logout
- [ ] Persistência da sessão
- [ ] Proteção de rotas
- [ ] Hash de senha
- [ ] Validação dos dados

### Usuário

- [ ] Nome
- [ ] E-mail
- [ ] Senha
- [ ] Data de criação

### Lançamentos

- [ ] Registrar receita
- [ ] Registrar despesa
- [ ] Valor
- [ ] Data
- [ ] Categoria
- [ ] Descrição opcional
- [ ] Observação opcional
- [ ] Forma de pagamento
- [ ] Editar lançamento
- [ ] Excluir lançamento

### Categorias

Categorias pré-cadastradas.

#### Receitas

- Salário
- Freelance
- Investimento
- Benefício
- Outros

#### Despesas

- Alimentação
- Transporte
- Moradia
- Saúde
- Lazer
- Educação
- Roupas
- Outros

### Formas de pagamento

- Pix
- Débito
- Crédito
- Dinheiro

> **Importante:** `Crédito` no MVP representa apenas a forma de pagamento. Não haverá módulo de cartão, fatura, limite ou parcelamento.

### Dashboard

- [ ] Resultado do mês
- [ ] Total de receitas
- [ ] Total de despesas
- [ ] Comprometimento da renda
- [ ] Distribuição de despesas por categoria
- [ ] Comparação com o mês anterior
- [ ] Lançamentos recentes

### Estados da aplicação

- [ ] Loading
- [ ] Empty
- [ ] Success
- [ ] Error
- [ ] Retry

---

## Fora do MVP

### 🟡 V1.1

- [ ] Categorias personalizadas
- [ ] Filtros avançados
- [ ] Gráficos adicionais
- [ ] Orçamento mensal
- [ ] Metas financeiras
- [ ] Lançamentos recorrentes
- [ ] Exportação CSV
- [ ] Recuperação de senha
- [ ] Contas bancárias independentes
- [ ] Transferências
- [ ] Cartão de crédito com fatura
- [ ] Parcelamento

### 🟢 Futuro

- [ ] Open Finance
- [ ] Integração bancária
- [ ] Investimentos
- [ ] Criptomoedas
- [ ] OCR de notas fiscais
- [ ] IA
- [ ] Múltiplas moedas
- [ ] Automação bancária
- [ ] Planejamento financeiro avançado

**Regra de escopo:** nenhuma funcionalidade V1.1 ou Futuro deve ser incorporada ao MVP sem substituir explicitamente outra funcionalidade e revisar o prazo.

---

## Regras de negócio

### RN01 — Tipos de lançamento

O MVP possui somente:

```text
INCOME
EXPENSE
```

### RN02 — Valor

Todo lançamento deve possuir:

```text
amount > 0
```

O valor não recebe sinal negativo. O tipo define o efeito financeiro.

### RN03 — Receita

Receita aumenta o resultado do período.

### RN04 — Despesa

Despesa reduz o resultado do período.

### RN05 — Resultado do período

```text
resultado = receitas - despesas
```

### RN06 — Comprometimento da renda

```text
comprometimento = despesas / receitas × 100
```

Se `receitas == 0`, exibir `—`.

### RN07 — Período do dashboard

O dashboard mensal considera somente lançamentos pertencentes ao mês selecionado.

### RN08 — Comparação mensal

```text
variação = (valor_atual - valor_anterior) / valor_anterior × 100
```

Se o valor anterior for zero, exibir `—`.

### RN09 — Distribuição por categoria

O gráfico considera somente despesas e agrupa os valores por categoria.

### RN10 — Compatibilidade de categoria

Categorias de receita somente podem ser usadas em `INCOME`.

Categorias de despesa somente podem ser usadas em `EXPENSE`.

### RN11 — Propriedade dos dados

Um usuário somente pode consultar, editar ou excluir seus próprios lançamentos.

Essa regra deve ser validada no backend.

### RN12 — Descrição

A descrição é opcional.

### RN13 — Observação

A observação é opcional.

### RN14 — Data

Todo lançamento deve possuir uma data válida.

Datas futuras podem ser aceitas, mas o lançamento pertence ao seu próprio período e não entra no dashboard de outro mês.

### RN15 — Edição

O proprietário pode editar seus lançamentos.

Os indicadores devem ser recalculados após a alteração.

### RN16 — Exclusão

O proprietário pode excluir seus lançamentos.

Os indicadores devem ser recalculados após a exclusão.

### RN17 — Forma de pagamento

Despesas podem utilizar:

```text
PIX
DEBIT
CREDIT
CASH
```

### RN18 — Categorias

As categorias são pré-cadastradas pelo sistema.

O usuário não cria nem exclui categorias no MVP.

### RN19 — Transferências

Transferências não fazem parte do MVP.

### RN20 — Contas

Contas bancárias independentes não fazem parte do MVP.

Portanto, o resultado financeiro do Orbe é derivado dos lançamentos registrados e não representa necessariamente o saldo real de uma conta bancária.

### RN21 — Usuário sem lançamentos

Sem lançamentos, apresentar o estado Empty e a ação para adicionar o primeiro lançamento.

### RN22 — Estados

A aplicação deve tratar:

```text
LOADING
EMPTY
SUCCESS
ERROR
```

No erro, apresentar a ação de tentar novamente.

### RN23 — Logout

O logout encerra a sessão local e retorna o usuário ao fluxo de autenticação.

---

## Decisão importante: Resultado do mês

O protótipo inicialmente utilizava o termo:

> Saldo disponível

Para o MVP, o conceito será tratado como:

> **Resultado do mês**

Porque:

```text
resultado = receitas - despesas
```

e o sistema não possui, nesta versão:

- contas bancárias;
- saldo inicial;
- integração bancária;
- transferências entre contas.

Portanto, não devemos apresentar esse valor como o saldo real disponível em uma conta.

---

## Arquitetura

Stack inicial congelada para o MVP:

```text
React Native + Expo
        │
        │ REST / JSON
        ▼
FastAPI
        │
        │ ORM / SQL
        ▼
PostgreSQL
```

### Tecnologias

- React Native
- Expo
- Python
- FastAPI
- PostgreSQL
- JWT
- Git
- GitHub

### Observação sobre MySQL

MySQL também seria tecnicamente adequado ao projeto.

A decisão atual é permanecer com PostgreSQL para evitar retrabalho e manter o foco na entrega. A troca de banco não traz benefício suficiente para justificar a mudança neste momento.

Nginx não é obrigatório durante o desenvolvimento do MVP. Será utilizado somente se necessário no ambiente de deploy.

---

## Modelo de dados

### User

```text
id
name
email
password_hash
created_at
```

### Category

```text
id
name
type
```

### Transaction

```text
id
user_id
category_id
type
amount
description
date
payment_method
observation
created_at
updated_at
```

Relacionamentos:

```text
User 1 ─────── N Transaction

Category 1 ─── N Transaction
```

---

## Casos de uso

- [ ] UC01 — Cadastrar usuário
- [ ] UC02 — Autenticar usuário
- [ ] UC03 — Encerrar sessão
- [ ] UC04 — Consultar dashboard
- [ ] UC05 — Registrar receita
- [ ] UC06 — Registrar despesa
- [ ] UC07 — Consultar lançamentos
- [ ] UC08 — Editar lançamento
- [ ] UC09 — Excluir lançamento
- [ ] UC10 — Calcular resultado do período
- [ ] UC11 — Calcular comprometimento da renda
- [ ] UC12 — Calcular distribuição por categoria
- [ ] UC13 — Calcular comparação mensal

---

# TODO — 4 semanas

## Semana 1 — Backend e domínio

### Infraestrutura

- [ ] Criar estrutura do backend
- [ ] Configurar ambiente virtual
- [ ] Configurar variáveis de ambiente
- [ ] Configurar PostgreSQL
- [ ] Configurar SQLAlchemy
- [ ] Configurar migrations
- [ ] Criar estrutura inicial do projeto

### Banco

- [ ] Criar tabela `users`
- [ ] Criar tabela `categories`
- [ ] Criar tabela `transactions`
- [ ] Criar relacionamentos
- [ ] Criar categorias padrão
- [ ] Criar migrations

### Autenticação

- [ ] Endpoint de cadastro
- [ ] Hash de senha
- [ ] Endpoint de login
- [ ] JWT
- [ ] Dependência de usuário autenticado
- [ ] Proteção dos endpoints

### Transações

- [ ] Criar receita
- [ ] Criar despesa
- [ ] Listar lançamentos
- [ ] Validar categoria
- [ ] Validar valor
- [ ] Validar usuário proprietário

### Dashboard

- [ ] Endpoint de resumo
- [ ] Total de receitas
- [ ] Total de despesas
- [ ] Resultado
- [ ] Comprometimento
- [ ] Distribuição por categoria
- [ ] Comparação mensal

### Testes iniciais

- [ ] Testar cadastro
- [ ] Testar login
- [ ] Testar autenticação
- [ ] Testar criação de receita
- [ ] Testar criação de despesa
- [ ] Testar cálculos

---

## Semana 2 — Mobile e integração

### Navegação

- [ ] Configurar navegação
- [ ] Fluxo de autenticação
- [ ] Fluxo autenticado

### Autenticação

- [ ] Tela de login
- [ ] Tela de cadastro
- [ ] Persistência do token
- [ ] Logout

### Dashboard

- [ ] Implementar dashboard
- [ ] Consumir API
- [ ] Mostrar resultado
- [ ] Mostrar receitas
- [ ] Mostrar despesas
- [ ] Mostrar comprometimento
- [ ] Mostrar distribuição

### Lançamentos

- [ ] Tela de seleção Receita/Despesa
- [ ] Tela de receita
- [ ] Tela de despesa
- [ ] Seleção de categoria
- [ ] Seleção de forma de pagamento
- [ ] Envio para API

### Estados

- [ ] Loading
- [ ] Empty
- [ ] Error
- [ ] Retry

---

## Semana 3 — Histórico e refinamento

### Histórico

- [ ] Listar lançamentos
- [ ] Mostrar descrição
- [ ] Mostrar categoria
- [ ] Mostrar data
- [ ] Mostrar valor

### Edição

- [ ] Endpoint de edição
- [ ] Tela/fluxo de edição
- [ ] Recalcular dashboard

### Exclusão

- [ ] Endpoint de exclusão
- [ ] Confirmação de exclusão
- [ ] Recalcular dashboard

### Dashboard

- [ ] Comparação mensal
- [ ] Distribuição por categoria
- [ ] Refinar gráficos
- [ ] Validar cálculos

### Testes

- [ ] Testes de API
- [ ] Testes de autenticação
- [ ] Testes de transações
- [ ] Testes de dashboard
- [ ] Testes de autorização
- [ ] Testes de erros

### UX

- [ ] Validar formulários
- [ ] Mensagens de erro
- [ ] Feedback de sucesso
- [ ] Revisar navegação
- [ ] Revisar responsividade

---

## Semana 4 — Estabilização e entrega

### Testes finais

- [ ] Fluxo completo de cadastro
- [ ] Fluxo completo de login
- [ ] Fluxo completo de receita
- [ ] Fluxo completo de despesa
- [ ] Fluxo completo de dashboard
- [ ] Fluxo completo de histórico
- [ ] Edição
- [ ] Exclusão
- [ ] Logout
- [ ] Testar usuário sem dados
- [ ] Testar erro de API
- [ ] Testar perda de conexão
- [ ] Testar autorização

### Segurança

- [ ] Revisar armazenamento de senha
- [ ] Revisar JWT
- [ ] Revisar autorização
- [ ] Revisar variáveis de ambiente
- [ ] Remover secrets do Git
- [ ] Revisar CORS

### Documentação

- [ ] Atualizar README
- [ ] Documentar instalação
- [ ] Documentar variáveis de ambiente
- [ ] Documentar execução backend
- [ ] Documentar execução mobile
- [ ] Documentar API
- [ ] Documentar regras principais

### Entrega

- [ ] Gerar build
- [ ] Testar build
- [ ] Preparar demonstração
- [ ] Preparar apresentação
- [ ] Ensaiar fluxo de demonstração
- [ ] Fazer backup/tag da versão final
- [ ] Criar release do MVP

---

## Definition of Done

O MVP será considerado concluído quando:

- [ ] Cadastro funciona
- [ ] Login funciona
- [ ] Logout funciona
- [ ] Senhas não são armazenadas em texto puro
- [ ] Usuários não acessam dados uns dos outros
- [ ] Receitas são persistidas
- [ ] Despesas são persistidas
- [ ] Edição funciona
- [ ] Exclusão funciona
- [ ] Dashboard calcula corretamente
- [ ] Comprometimento trata receita zero
- [ ] Distribuição por categoria funciona
- [ ] Comparação mensal funciona
- [ ] Loading funciona
- [ ] Empty funciona
- [ ] Error funciona
- [ ] Retry funciona
- [ ] Mobile conversa com a API real
- [ ] Testes mínimos estão passando
- [ ] README está atualizado
- [ ] Build demonstrável está funcionando

---

## Regra de ouro do projeto

> **Se uma nova ideia não for necessária para o fluxo principal do MVP, ela vai para V1.1 ou Futuro.**

O objetivo das próximas quatro semanas não é construir o aplicativo financeiro definitivo.

É construir um **MVP funcional, consistente, testado e demonstrável**.
