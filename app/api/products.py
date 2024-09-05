from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_async_session
from app.crud.product import get_product_by_id, create_product
from app.schemas.product import ProductSchema


router = APIRouter(
    prefix='/product',
    tags=['Product'],
)


@router.get('/')
async def create_new_product(
    nm_id: int,
    product: ProductSchema,
    session: AsyncSession = Depends(get_async_session),
):
    """Функция получения нового продукта и его записи в базу, если его нет."""
    product = await get_product_by_id(nm_id, session)
    if product:
        return product
    print(product)
    new_product = await create_product(product, session)
    return new_product
