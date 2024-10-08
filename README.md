# Проект test-api-bot
Проект представляет собой 2 отдельных приложения (API и телеграм-бот). Функционал позволяет получить информацию о товаре с Wildberries по ID товара.
СУБД - PostgreSQL. Оба приложения, а также база поднимаются в отдельных контейнерах.

Бот отправляет данные в человекочитаемом виде а также отправляет пользователю картинку товара.
Пример ответа:
```
Данные по товару номер 209054252:

Цена - 990,
Всего остатков товара (все размеры) - 1514

Имеющиеся размеры и остатки по складам:

Размер 38:
Номер склада - 208782.Остатки на складе - 100 шт.
Номер склада - 507.Остатки на складе - 1 шт.

Размер 40:
Номер склада - 208782.Остатки на складе - 100 шт.
Номер склада - 507.Остатки на складе - 2 шт.

Размер 42:
Номер склада - 208782.Остатки на складе - 100 шт.
Номер склада - 206348.Остатки на складе - 1 шт.
```

API отдает данные в следующем виде (пример):
```
{
    "nm_id": 166690984,
    "current_price": 603,
    "sum_quantity": 4508,
    "image_url": "https://basket-12.wbbasket.ru/vol1666/part166690/166690984/images/big/1.webp",
    "quantity_by_sizes": [
        {
            "size": "46",
            "quantity_by_wh": [
                {
                    "wh": 507,
                    "quantity": 200
                },
                {
                    "wh": 130744,
                    "quantity": 123
                },
            ]
        },
        {
            "size": "48",
            "quantity_by_wh": [
                {
                    "wh": 507,
                    "quantity": 170
                },
                {
                    "wh": 1733,
                    "quantity": 1
                },
            ]
        }
    ]
}
```
## Краткое описание подхода:
* Бот реализован с двумя хэндлерами. Первый обратабывает только команду /start и отправляет пользователю краткую инструкцию. Второй - проверяет корректность введенного ID товара, существует ли такой товар в принципе (до отправки GET-запроса в API) и отправляет пользователю человекочитаемые данные. Если такого товара нет на Wildberries - запрос не попадет в API и пользователь будет оповещен о том, что такого товара не существует. При наличии товара - запрос отправляется в API.
* API принимает GET-запрос с ID товара. Пример ```http://127.0.0.1:8000/product/166690984```.
После чего проверятеся наличие товара в базе. Если его нет, вызывается функция создания товара.
Для этого реализованы вспомогательные функции (для получения данных о товаре, конвертации этих данных и получения ссылки на картинку товара). Товар создается в базе и ответом на запрос отправляются данные, которые затем будут конвертированы ботом в человекочитаемый формат и отправлены пользователю.

## Стек:
FastAPI, Pydantic, PostgreSQL, SQLAlchemy 2 + Alembic, Aiogram, Docker, docker-compose.

## Инструкция по запуску:
Клонировать репозиторий и перейти в него в командной строке:
  
```
git@github.com:VDronovVladislav/test-api-bot.git
```

Отредактировать .env файл. Шаблон наполнения:
```
APP_TITLE=Получение/запись в базов товарос в WB.
DATABASE_URL=postgresql+asyncpg://postgres:postgres@product_db:5432/product
TELEGRAM_TOKEN='Тут ваш токен'

POSTGRES_USER=postgres # логин для подключения к базе данных
POSTGRES_PASSWORD=postgres # пароль для подключения к БД (установите свой)
POSTGRES_DB=product # имя базы данных
DB_HOST=db_product # название сервиса (контейнера)
DB_PORT=5432 # порт для подключения к БД
```
Запустить docker-compose командой:
```
docker-compose up -d
```

Остановить контейнеры можно командой:
```
docker-compose down -v
```

Лиценция:
```
MIT License
```
