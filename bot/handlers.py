from aiogram import Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message

from api_client import get_product_info


dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    """Хэндлер для комманды /start."""
    await message.answer(
        f'''
        Привет {message.from_user.full_name}!
        Пришли мне ID товара и я пришлю тебе информацию о нем.
        '''
    )


@dp.message()
async def message_handler(message: Message) -> None:
    """Хэндлер с обработкой nm_id и проверкой существует ли товар."""
    nm_id = message.text
    try:
        int(nm_id)
    except ValueError:
        await message.answer('Отправьте ID в числовом формате!')
        return

    product_info = await get_product_info(str(nm_id))
    if product_info is True:
        print('Все окей')
    else:
        await message.answer(
                f'Товара с таким ID: {nm_id} - не существует!'
            )
