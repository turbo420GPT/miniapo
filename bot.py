import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
import asyncio
from database import init_db, add_user, update_balance, get_top_users, get_balance

API_TOKEN = '7936064458:AAF9nK8kQ-anW1wUCzqJrb69ePjGI7UVPXk'

# Настройки логирования
logging.basicConfig(level=logging.INFO)

# Инициализация бота и диспетчера
bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# Инициализация базы данных
init_db()

# Команда старт
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    username = message.from_user.username or message.from_user.first_name
    add_user(username)
    await message.reply(f"Добро пожаловать, {username}! Нажмите /click, чтобы начать кликер.")

# Команда клик
@dp.message(Command("click"))
async def cmd_click(message: types.Message):
    username = message.from_user.username or message.from_user.first_name
    update_balance(username, 1)  # Увеличиваем баланс на 1
    balance = get_balance(username)
    await message.reply(f"Клик! Ваш баланс: {balance}.")

# Команда топ
@dp.message(Command("top"))
async def cmd_top(message: types.Message):
    top_users = get_top_users(15)
    top_message = "Топ 15 игроков:\n"
    for rank, (username, balance) in enumerate(top_users, 1):
        top_message += f"{rank}. {username} - {balance}\n"
    await message.reply(top_message)

# Асинхронная функция для запуска бота
async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.info("Бот запущен")
    asyncio.run(main())
