import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command


logging.basicConfig(level=logging.INFO)


API_TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN'


bot = Bot(token=API_TOKEN)
dp = Dispatcher()


@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("hello world!")


@dp.message(Command("help"))
async def cmd_help(message: types.Message):
    await message.answer("Это помощь.")


@dp.message(content_types=types.ContentTypes.TEXT)
async def echo(message: types.Message):
    await message.reply(f"Вы сказали: {message.text}")

async def main():
    await dp.start_polling(bot)

# Запускаем бота
if __name__ == '__main__':
    asyncio.run(main())
