import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('TELEGRAM_TOKEN')
BASE_URL = "https://card.wb.ru/cards/v2/detail"
PARAMS = {
        "appType": 1,
        "curr": "rub",
        "dest": "123585476",
        "spp": 30,
        "ab_testing": "false",
    }
API_URL = 'http://127.0.0.1:8000/product'

IMAGE_URL = 'https://www.wildberries.ru/catalog'

BASKETS = {
    range(0, 144): "https://basket-01.wbbasket.ru",
    range(144, 288): "https://basket-02.wbbasket.ru",
    range(288, 432): "https://basket-03.wbbasket.ru",
    range(432, 720): "https://basket-04.wbbasket.ru",
    range(720, 1008): "https://basket-05.wbbasket.ru",
    range(1008, 1062): "https://basket-06.wbbasket.ru",
    range(1062, 1116): "https://basket-07.wbbasket.ru",
    range(1116, 1170): "https://basket-08.wbbasket.ru",
    range(1170, 1314): "https://basket-09.wbbasket.ru",
    range(1314, 1602): "https://basket-10.wbbasket.ru",
    range(1602, 1656): "https://basket-11.wbbasket.ru",
    range(1656, 1920): "https://basket-12.wbbasket.ru",
    range(1920, 2046): "https://basket-13.wbbasket.ru",
    "default": "https://basket-14.wbbasket.ru"
}
