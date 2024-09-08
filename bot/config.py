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
