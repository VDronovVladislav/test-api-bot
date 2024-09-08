from config import BASKETS


def get_image_url(nm_id: int):
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


def data_converter_for_bot(response):
    """Отдает данные по товару в человекочитаемом виде."""
    sizes_info = []
    for size_data in response['quantity_by_sizes']:
        size = size_data['size']
        warehouses = size_data['quantity_by_wh']
        size_info = f"Размер {size}:\n"
        if not warehouses:
            size_info += 'Нет в наличии.\n'

        for wh in warehouses:
            wh_number = wh['wh']
            quantity = wh['quantity']
            size_info += (f"Номер склада - {wh_number}."
                          f"Остатки на складе - {quantity} шт.\n")

        sizes_info.append(size_info)

    sizes_info_str = '\n'.join(sizes_info)

    message = f"""
Данные по товару номер {response['nm_id']}:

Цена - {response['current_price']},
Всего остатков товара (все размеры) - {response['sum_quantity']}

Имеющиеся размеры и остатки по складам:

{sizes_info_str}
"""
    return message
