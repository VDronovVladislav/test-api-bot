import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('TELEGRAM_TOKEN')
PREFIX_URL = 'https://basket-01.wbbasket.ru'
BASE_URL = "https://card.wb.ru/cards/v2/detail"
PARAMS = {
        "appType": 1,
        "curr": "rub",
        "dest": "123585476",
        "spp": 30,
        "ab_testing": "false",
    }
