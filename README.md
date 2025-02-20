# Documentação da API com uso de IA

A **API de E-commerce** foi desenvolvida com o framework **FastAPI** para gerenciar produtos em um e-commerce. Ela oferece cinco endpoints principais: criar, listar, buscar, atualizar e deletar produtos. A API utiliza um banco de dados em memória simples para armazenar os produtos.

## Conhecimentos Aprendidos

- **FastAPI**: Como criar uma API rápida e eficiente com FastAPI.
- **EndPoints RESTful**: Como criar endpoints para CRUD (Create, Read, Update, Delete).
- **Pydantic**: Como usar modelos de dados com validação automática.

## Funções
1. Listar produtos: Para retornar todos os produtos do e-commerce.
2. Criar produto: Para adicionar um novo produto ao catálogo.
3. Buscar produto: Para buscar um produto específico pelo seu ID.
4. Atualizar produto: Para atualizar as informações de um produto.
5. Deletar produto: Para excluir um produto do catálogo.

## Estrutura do projeto
```bash
ecommerce/
  |__ main.py
  |__ models.py
```

## Requisitos
- Python
- FastAPI
- Pydantic
- Typing
- Uvicorn

## Como executar
Passo 1: Instalando as dependências

Primeiro, instale o FastAPI e o Uvicorn (para rodar o servidor):
```bash
pip install fastapi uvicorn typing pydantic
```

Passo 2: Clone o repositório da api
```bash
git clone [url repositorio]
```

Passo 3: Rodando a API

Para rodar a API, basta executar o seguinte comando:
```bash
uvicorn main:app --reload
```
A API estará disponível em http://127.0.0.1:8000


## Endpoints:

1 - Criar um novo produto.
- URL: /products/
- Método: POST
- Corpo da requisição (JSON):
```json
{
  "name": "Produto A",
  "description": "Descrição do produto A",
  "price": 100.50,
  "quantity": 10
}
```
- Resposta (JSON):
```json
{
  "id": 1,
  "name": "Produto A",
  "description": "Descrição do produto A",
  "price": 100.5,
  "quantity": 10
}
```

2 - Listar todos os produtos.
- URL: /products/
- Método: GET
- Resposta (JSON):
 ```json
   [{
    "id": 1,
    "name": "Produto A",
    "description": "Descrição do produto A",
    "price": 100.5,
    "quantity": 10
  }]
```

3 - Buscar um produto específico.
- URL: /products/{product_id}
- Método: GET
- Parâmetros de URL:
  - product_id: ID do produto a ser buscado.
- Resposta (JSON):
```json
{
  "id": 1,
  "name": "Produto A",
  "description": "Descrição do produto A",
  "price": 100.5,
  "quantity": 10
}
```

4 - PUT /products/{product_id} - Atualizar um produto existente.
- URL: /products/{product_id}
- Método: PUT
- Corpo da requisição (JSON):
```json
{
  "name": "Produto A Atualizado",
  "description": "Descrição atualizada",
  "price": 120.0,
  "quantity": 15
}
```

 - Resposta (JSON):
```json
{
  "id": 1,
  "name": "Produto A Atualizado",
  "description": "Descrição atualizada",
  "price": 120.0,
  "quantity": 15
}
```

5 - Deletar um produto.
- URL: /products/{product_id}
- Método: DELETE
- Parâmetros de URL:

  - product_id: ID do produto a ser deletado.

- Resposta (JSON):

```json
  {
  "id": 1,
  "name": "Produto A",
  "description": "Descrição do produto A",
  "price": 100.5,
  "quantity": 10
  }
```
