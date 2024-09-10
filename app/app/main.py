import asyncio

from fastapi import FastAPI

from app.core.utils import main_product_data
from app.crud.product import update_product, get_all_products
from app.core.db import get_async_session

from app.core.config import settings
from app.api.products import router

app = FastAPI(title=settings.app_title)


async def update_all_products(session_maker):
    """Фоновая задача для обновления данных о всех товарах каждые 5 минут."""
    while True:
        async with session_maker() as session:
            products = await get_all_products(session)

            for product in products:
                nm_id = product.nm_id
                product_data = await main_product_data(nm_id)
                await update_product(product_data, session)

        await asyncio.sleep(300)


@app.on_event("startup")
async def startup_event():
    """Запуск фоновой задачи при старте приложения."""
    session_maker = get_async_session
    asyncio.create_task(update_all_products(session_maker))


app.include_router(router)
