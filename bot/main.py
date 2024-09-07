import asyncio

from aiogram import Bot
from aiogram.client.default import DefaultBotProperties

from config import TOKEN
from handlers import dp


async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode='HTML'))
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
