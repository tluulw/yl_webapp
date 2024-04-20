import asyncio
import logging
import os

from aiogram import Bot, Dispatcher
from aiogram.filters.command import Command
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo, LabeledPrice
from dotenv import load_dotenv

load_dotenv()

dp = Dispatcher()

kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Каталог',
                          web_app=WebAppInfo(
                              url='https://5b30cbb6-8b1b-45db-800f-9d8b416bad01.tunnel4.com/menu'))]
])

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)

BOT_TOKEN = os.getenv("BOT_TOKEN")
PROVIDER_TOKEN = os.getenv("PROVIDER_TOKEN")
bot = Bot(BOT_TOKEN)


@dp.message(Command('menu'))
async def echo(message: Message):
    await message.answer('Посмотреть каталог:', reply_markup=kb)


async def main() -> None:
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Bye bye')
