import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

# .env faylini yuklash
load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start_cmd(msg: types.Message):
    await msg.reply("Salom! Bot ishga tushdi.")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)