from typing import List, Annotated

from pydantic import BaseModel, Field


class ProductResponse(BaseModel):
    product_id: int
    name: Annotated[str, Field(max_length=100)]
    price: float
    in_stock: bool

    class Config:
        from_attributes = True


class ProductCreate(BaseModel):
    category_id: int
    name: Annotated[str, Field(max_length=100)]
    price: float
    in_stock: Annotated[bool, Field(True)]


class CategoryReponse(BaseModel):
    category_id: int
    name: Annotated[str, Field(max_length=100)]
    description: str | None = None
    products: Annotated[List[ProductResponse], []]

    class Config:
        from_attributes = True


class CategoryCreate(BaseModel):
    name: Annotated[str, Field(min_length=2, max_length=100)]
    description: Annotated[str, Field(None, max_length=500)]


class CategoryUpdate(BaseModel):
    name: Annotated[str, Field(None, min_length=2, max_length=100)]
    description: Annotated[str, Field(None, max_length=500)]
