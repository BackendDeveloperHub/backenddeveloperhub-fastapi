from fastapi import APIRouter
from schemas.products import ProductResponse, ProductCreate

router = APIRouter()

@router.post('/products', response_model=ProductResponse)
async def product_create(product: ProductCreate):
    return {'id': 1, 'name': product.name, 'price': product.price}