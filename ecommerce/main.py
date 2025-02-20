# main.py

from fastapi import FastAPI, HTTPException
from models import Product, ProductCreate
from typing import List

app = FastAPI()

# Banco de dados simples em memória (dicionário)
fake_db = {}

@app.post("/products/", response_model=Product)
def create_product(product: ProductCreate):
    product_id = len(fake_db) + 1
    new_product = Product(id=product_id, **product.dict())
    fake_db[product_id] = new_product
    return new_product

@app.get("/products/", response_model=List[Product])
def get_products():
    return list(fake_db.values())

@app.get("/products/{product_id}", response_model=Product)
def get_product(product_id: int):
    if product_id not in fake_db:
        raise HTTPException(status_code=404, detail="Product not found")
    return fake_db[product_id]

@app.put("/products/{product_id}", response_model=Product)
def update_product(product_id: int, product: ProductCreate):
    if product_id not in fake_db:
        raise HTTPException(status_code=404, detail="Product not found")
    updated_product = Product(id=product_id, **product.dict())
    fake_db[product_id] = updated_product
    return updated_product

@app.delete("/products/{product_id}", response_model=Product)
def delete_product(product_id: int):
    if product_id not in fake_db:
        raise HTTPException(status_code=404, detail="Product not found")
    deleted_product = fake_db.pop(product_id)
    return deleted_product
