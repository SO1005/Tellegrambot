import asyncio
from aiogram import Bot, Dispatcher, types

TOKEN = "7560552632:AAGKtr8DvHqXL_oYoykD4xUu9YmMovTMHuM"

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message()
async def echo(message: types.Message):
    await message.answer(message.text)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

