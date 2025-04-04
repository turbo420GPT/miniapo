import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
import asyncio

API_TOKEN = '7936064458:AAF9nK8kQ-anW1wUCzqJrb69ePjGI7UVPXk'

# Настройки логирования
logging.basicConfig(level=logging.INFO)

# Инициализация бота и диспетчера
bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# Команда старт
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.reply("Добро пожаловать! Нажмите /click, чтобы начать кликер.")

# Команда клик
@dp.message(Command("click"))
async def cmd_click(message: types.Message):
    await message.reply("Клик! Теперь нажмите /click снова.")

# Асинхронная функция для запуска бота
async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.info("Бот запущен")
    asyncio.run(main())