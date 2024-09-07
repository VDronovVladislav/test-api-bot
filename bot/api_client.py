import aiohttp

from config import BASE_URL, PARAMS


async def get_product_info(nm_id: str) -> bool:
    """Функция проверки наличия товара."""
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
