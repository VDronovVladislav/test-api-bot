from typing import Dict, Any
import aiohttp

from config import BASE_URL, PARAMS, API_URL


async def get_product_info(nm_id: str) -> bool:
    """Функция проверки наличия товара на WB."""
    PARAMS["nm"] = nm_id
    async with aiohttp.ClientSession() as session:
        response = await session.get(BASE_URL, params=PARAMS)
        product_data = await response.json()
        if product_data['data']['products']:
            return True
        elif not product_data['data']['products']:
            return False
        else:
            response.raise_for_status()


async def get_db_product_info(nm_id: str) -> Dict[str, Any]:
    """Функция получения информации о товаре из БД."""
    async with aiohttp.ClientSession() as session:
        api_url = f"{API_URL}/{nm_id}"
        response = await session.get(api_url)
        return await response.json()
