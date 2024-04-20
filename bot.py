import asyncio
import logging
import os

from aiogram import Bot, Dispatcher
from aiogram.filters.command import Command
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from dotenv import load_dotenv

load_dotenv()

dp = Dispatcher()

reviews_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Отзывы',
                          web_app=WebAppInfo(
                              url='https://11b7a6b9-812e-42b0-ae6e-766d0b53b7d1.tunnel4.com/reviews'))]
])

menu_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Каталог',
                          web_app=WebAppInfo(
                              url='https://11b7a6b9-812e-42b0-ae6e-766d0b53b7d1.tunnel4.com/menu'))]
])

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)

BOT_TOKEN = os.getenv("BOT_TOKEN")
PROVIDER_TOKEN = os.getenv("PROVIDER_TOKEN")
bot = Bot(BOT_TOKEN)


@dp.message(Command('start'))
async def echo(message: Message):
    await message.answer(
        'Здравствуйте! Для использования корзины и бота нажмите на кнопку "Меню", рядом с полем ввода текста 👇')
    await message.answer('Для написания вашего первого отзыва введите команду /reviews')


@dp.message(Command('menu'))
async def echo(message: Message):
    await message.answer('Посмотреть каталог:', reply_markup=menu_kb)


@dp.message(Command('reviews'))
async def echo(message: Message):
    await message.answer('Посмотреть отзывы:', reply_markup=reviews_kb)


@dp.message()
async def echo(message: Message):
    await message.answer('Не понял вас... Пожалуйста, введите команду, предложенных: /start /reviews')


async def main() -> None:
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Bye bye')
