import asyncio
import logging
import os

from aiogram import Bot, Dispatcher, F
from aiogram.filters.command import Command
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo, PreCheckoutQuery
from dotenv import load_dotenv

load_dotenv()

dp = Dispatcher()

reviews_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Отзывы',
                          web_app=WebAppInfo(
                              url='https://yl-webapp.onrender.com/reviews'))]
])

menu_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Меню',
                          web_app=WebAppInfo(
                              url='https://yl-webapp.onrender.com/menu'))]
])

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)

BOT_TOKEN = os.getenv("BOT_TOKEN")
bot = Bot(BOT_TOKEN)


@dp.message(Command('start'))
async def echo(message: Message):
    await message.answer(
        'Здравствуйте! Для использования корзины и бота нажмите на кнопку "Меню", рядом с полем ввода текста 👇')
    await message.answer('Для написания вашего первого отзыва введите команду /reviews')


@dp.message(Command('menu'))
async def echo(message: Message):
    await message.answer('Посмотреть меню:', reply_markup=menu_kb)


@dp.message(Command('reviews'))
async def echo(message: Message):
    await message.answer('Написать отзыв:', reply_markup=reviews_kb)


@dp.pre_checkout_query()
async def pre_checkout_query(pre_checkout_query: PreCheckoutQuery):
    await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)


@dp.message(F.successful_payment)
async def successful_payment(message: Message):
    await message.answer('Оплата прошла успешно!')
    await message.answer('Благодарим за заказ!')


async def main() -> None:
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Bye bye')
