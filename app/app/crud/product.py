from typing import Optional

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi.encoders import jsonable_encoder

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
    db_product = Product(**new_product)
    session.add(db_product)
    await session.commit()
    await session.refresh(db_product)
    return db_product


async def get_all_products(
        session: AsyncSession
) -> list[Product]:
    """CRUD-фунуция получения всех товаров."""
    products = await session.execute(select(Product))
    return products.scalars.all()


async def update_product(
        db_product: Product,
        product_in: ProductSchema,
        session: AsyncSession
) -> None:
    obj_data = jsonable_encoder(db_product)
    update_data = product_in.model_dump(exclude_unset=True)

    for field in obj_data:
        if field in update_data:
            setattr(db_product, field, update_data[field])

    session.add(db_product)
    await session.commit()
    await session.refresh(db_product)
