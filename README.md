# 📚 API Biblioteca - Projeto FastAPI

Este projeto consiste no desenvolvimento de uma API RESTful para controle de **livros**, **clientes** e **empréstimos** de uma biblioteca, com armazenamento **em memória**, sem uso de banco de dados. O objetivo é aplicar os conceitos fundamentais de APIs RESTful com FastAPI, conforme os critérios definidos para obtenção do conceito **C**.

---

## 🚀 Tecnologias Utilizadas

- **Python 3.11**
- **FastAPI**
- **Pydantic**
- **Uvicorn**
- **Insomnia** (para testes das rotas)

---

## ✅ Funcionalidades Implementadas

### 📘 CRUD de Livros

- `GET /localizar` — Listar todos os livros
- `GET /localizar_livro/{isbn}` — Buscar livro pelo ISBN
- `POST /adicionar_livro` — Adicionar novo livro (ou aumentar quantidade, se já cadastrado)
- `PUT /editar_livro/{isbn}` — Atualizar dados de um livro
- `DELETE /deletar_livro/{isbn}` — Remover um livro

---

### 👤 CRUD de Clientes

- `GET /clientes` — Listar todos os clientes
- `GET /clientes/{matricula}` — Buscar cliente pela matrícula
- `POST /clientes` — Adicionar novo cliente (**matrícula gerada automaticamente**)
- `PUT /clientes/{matricula}` — Atualizar dados de um cliente
- `DELETE /clientes/{matricula}` — Remover um cliente

---

### 🔄 Funcionalidades da Biblioteca (Empréstimos e Devoluções)

- `POST /biblioteca/alugar/{matricula}/{isbn}` — Alugar um livro para um cliente  
  ↳ O cliente pode ter no máximo 3 livros alugados. O livro precisa estar disponível.

- `POST /biblioteca/devolver/{matricula}/{isbn}` — Devolver um livro  
  ↳ Atualiza a disponibilidade do livro, remove dos empréstimos e verifica atraso na devolução.

- `GET /biblioteca/emprestimos` — Listar todos os empréstimos ativos

- `GET /biblioteca/livros_disponiveis` — Listar todos os livros atualmente disponíveis para empréstimo

---

## 🧪 Testes

Todos os endpoints da API foram testados utilizando o **Insomnia**, cobrindo:

- Cadastro, edição, listagem, busca e remoção de livros e clientes
- Fluxo completo de aluguel e devolução de livros
- Verificação de limites (máximo 3 livros por cliente)
- Controle de disponibilidade dos livros

A coleção de testes foi exportada em formato `.json` e está incluída no projeto.

---

## 🗂 Estrutura de Pastas

Biblioteca/
├── app.py # Arquivo principal com as rotas da API
├── models/ # Modelos Pydantic
│ ├── Livro.py # Modelo para Livro
│ └── Cliente.py # Modelo para Cliente
├── services/ # Lógicas de negócio
│ ├── livros_Services.py # CRUD de livros
│ ├── cliente_services.py # CRUD de clientes
│ └── biblioteca_services.py # Controle de empréstimos e devoluções


---

## 📝 Como executar

1. **Crie o ambiente virtual:**

```bash
python -m venv .venv
source .venv/bin/activate   # Linux/Mac
.venv\Scripts\activate      # Windows


2. **Instale as dependências:**

pip install -r requirements.txt


3. **Rode a aplicação:**

uvicorn app:app --reload


4. **Acesse a documentação automática:**

http://localhost:8000/docs




📦 Entrega

    ✅ Código-fonte estruturado e funcional

    ✅ Dados mantidos em memória

    ✅ Testes realizados no Insomnia (arquivo .json incluído)

    ✅ CRUD completo de livros e clientes

    ✅ Funcionalidade de negócio implementada (empréstimos e devoluções)



