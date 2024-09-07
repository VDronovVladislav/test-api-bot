import requests
from pprint import pprint


import requests

def get_main_product(product_id):
    pass


def get_product_data(product_id):
    base_url = "https://card.wb.ru/cards/v2/detail"
    params = {
        "appType": 1,
        "curr": "rub",
        "dest": "123585476",
        "spp": 30,
        "ab_testing": "false",
        "nm": ";".join(product_id)
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()
        if data['data']['products']:
            print('данные есть')
            #print(response.json())
        #return response.json()
        else:
            print('Данных нет')
            return None


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



# Пример
product_id = ['209054252']
data = parse_data(get_product_data(product_id))

if data:
    print(data)
else:
    print("Failed to retrieve data")
