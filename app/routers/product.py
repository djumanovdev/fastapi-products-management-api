from typing import Annotated

from fastapi.routing import APIRouter
from fastapi import Body, Path, Query, Depends, HTTPException, status
from sqlalchemy.orm import Session

from ..schemas import ProductCreate, ProductResponse
from ..database import get_db
from ..models import Product, Category

router = APIRouter(tags=['Products'])


@router.get('/')
def get_products():
    return {}


@router.post('/', response_model=ProductResponse)
def create_product(
    # product_data: ProductCreate = Body(),
    product_data: Annotated[ProductCreate, Body],
    session: Annotated[Session, Depends(get_db)]
):
    category = session.query(Category).get(product_data.category_id)
    if category is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Category not found')
    
    product = Product(
        name=product_data.name,
        price=product_data.price,
        category_id=category.category_id,
        in_stock=product_data.in_stock
    )
    session.add(product)
    session.commit()
    session.refresh(product)

    return product
