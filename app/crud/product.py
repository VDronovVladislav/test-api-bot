from typing import Optional

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.product import Product
from app.schemas.product import ProductSchema


async def get_product_by_id(
        nm_id: int,
        session: AsyncSession,
) -> Optional[Product]:
    db_product = await session.execute(
        select(Product).where(
            Product.nm_id == nm_id
        )
    )
    db_product = db_product.scalars().first()
    return db_product
