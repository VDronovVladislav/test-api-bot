from typing import Optional

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.product import Product
from app.schemas.product import ProductSchema


async def get_product_by_id(
        nm_id: int,
        session: AsyncSession,
) -> Optional[Product]:
    """CRUD-функция получения товара по nm_id."""
    db_product = await session.execute(
        select(Product).where(
            Product.nm_id == nm_id
        )
    )
    db_product = db_product.scalars().first()
    return db_product


async def create_product(
        new_product: ProductSchema,
        session: AsyncSession
) -> Product:
    """CRUD-функция создания товара."""
    new_product_data = new_product.dict()
    db_product = Product(**new_product_data)
    session.add(db_product)
    await session.commit()
    await session.refresh(db_product)
    return db_product
