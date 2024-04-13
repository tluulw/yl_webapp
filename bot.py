import asyncio
import logging
import os

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from dotenv import load_dotenv

load_dotenv()

dp = Dispatcher()

kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Каталог',
                          web_app=WebAppInfo(
                              url='https://fd1971d9-c43f-4719-9da4-0b6d094de5c4.tunnel4.com/catalog/popular'))]
])

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)


@dp.message()
async def echo(message: Message):
    await message.answer('Посмотреть каталог:', reply_markup=kb)


async def main() -> None:
    BOT_TOKEN = os.getenv("BOT_TOKEN")
    # Initialize Bot instance with a default parse mode which will be passed to all API calls
    bot = Bot(BOT_TOKEN, parse_mode=ParseMode.HTML)
    # And the run events dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Bye bye')