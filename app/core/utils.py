from http import HTTPStatus

import aiohttp


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


def parse_data(response):
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
        "quantity_by_sizes": quantity_by_sizes,
    }
    return data


async def main_product_data(nm_id):
    data = await get_product_data(nm_id)
    return parse_data(data)
