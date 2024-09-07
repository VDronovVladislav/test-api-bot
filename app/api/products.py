from typing import Optional

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_async_session
from app.crud.product import get_product_by_id, create_product
from app.schemas.product import ProductSchema
from app.core.utils import main_product_data


router = APIRouter(
    prefix='/product',
    tags=['Product'],
)


@router.get(
        '/{nm_id}',
        response_model=ProductSchema
)
async def get_or_create_new_product(
    nm_id: int,
    session: AsyncSession = Depends(get_async_session),
):
    """Функция получения нового продукта и его записи в базу, если его нет."""
    product = await get_product_by_id(nm_id, session)
    if product:
        return product
    product_data = await main_product_data(nm_id)
    new_product = await create_product(product_data, session)
    return new_product
