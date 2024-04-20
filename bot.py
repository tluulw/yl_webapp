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
    [InlineKeyboardButton(text='Отзывы',
                          web_app=WebAppInfo(
                              url='https://reviewsitochka.glitch.me/reviews'))]
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
    await message.answer('Наши отзывы:', reply_markup=kb)


# async def create_invoice():
#     invoice_link = await bot.create_invoice_link(title='Оплата товара', description='Описание товара', payload='true',
#                                                  provider_token=PROVIDER_TOKEN, currency='rub',
#                                                  prices=[LabeledPrice(label='Покупка', amount=500 * 100)])
#     print(invoice_link)


async def main() -> None:
    # await create_invoice()
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Bye bye')
