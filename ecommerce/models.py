# models.py

from pydantic import BaseModel
from typing import List, Optional

# Definindo um modelo de Produto
class Product(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    price: float
    quantity: int

# Modelo para criação de produtos (sem o ID, que será gerado automaticamente)
class ProductCreate(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    quantity: int
