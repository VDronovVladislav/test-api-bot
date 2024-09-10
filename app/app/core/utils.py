from http import HTTPStatus
from typing import Any

import aiohttp

from app.core.constants import BASKETS


async def get_product_data(product_id):
    """Функция получения данных о товаре."""
    base_url = "https://card.wb.ru/cards/v2/detail"
    params = {
        "appType": 1,
        "curr": "rub",
        "dest": "123585476",
        "spp": 30,
        "ab_testing": "false",
        "nm": product_id
    }
    async with aiohttp.ClientSession() as session:
        response = await session.get(base_url, params=params)
        if response.status == HTTPStatus.OK:
            return await response.json()
        else:
            response.raise_for_status()


def get_image_url(nm_id: int) -> str:
    """Функция, формирующая url для картинки товара."""
    part = nm_id // 1000
    vol = part // 100
    suffix = 'images/big/1.webp'
    basket_url = BASKETS['default']

    for basket_range, url in BASKETS.items():
        if isinstance(basket_range, range) and vol in basket_range:
            basket_url = url
            break

    image_url = (
        f'{basket_url}/vol{str(vol)}/part{str(part)}/{str(nm_id)}/{suffix}'
    )
    return image_url


def parse_data(response) -> dict[str, Any]:
    """Функция, отдающая словарь значений."""
    product_data = response['data']['products'][0]
    sizes = product_data['sizes']

    quantity_by_sizes = [
        {
            "size": size['name'],
            "quantity_by_wh": [
                {
                    "wh": stock['wh'],
                    "quantity": stock['qty'],
                }
                for stock in size['stocks']
            ]
        }
        for size in sizes
    ]

    data = {
        "nm_id": product_data['id'],
        "current_price": int(sizes[0]['price']['total'] / 100),
        "sum_quantity": product_data['totalQuantity'],
        "image_url": get_image_url(product_data['id']),
        "quantity_by_sizes": quantity_by_sizes,
    }
    return data


async def main_product_data(nm_id):
    data = await get_product_data(nm_id)
    return parse_data(data)
