from pydantic import BaseModel
from typing import Optional, List

class ProductSchema(BaseModel):
    id: int
    name: str
    description: str
    price: float
    stock: int
    image_url: str

    model_config = {
    "from_attributes": True
    }

class ProductList(BaseModel):
    products: List[ProductSchema]

class ProductCreate(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    stock: int
    category_id: int
    image_url: Optional[str] = None

class CategoryCreate(BaseModel):
    category_id: Optional[int] = 0
    name: str

class ProductUpdate(BaseModel):
    name: Optional[str]
    description: Optional[str]
    price: Optional[float]
    stock: Optional[int]
    category_id: Optional[int]
    image_url: Optional[str]

class CategoryOut(BaseModel):
    id: int
    category_id: int
    name: str

    model_config = {
    "from_attributes": True
    }

class CategoryUpdate(BaseModel):
    category_id: Optional[int]
    name: Optional[str]
