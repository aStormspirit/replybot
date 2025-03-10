from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import logging
from dotenv import load_dotenv
import os

# Настройка логирования
logging.basicConfig(level=logging.INFO)
load_dotenv()

# Инициализация бота и диспетчера
BOT_TOKEN = os.getenv('BOT_TOKEN')
CHAT_ID = os.getenv('CHAT_ID')
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

# Создание клавиатуры
keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
button1 = KeyboardButton('Отчет')
button2 = KeyboardButton('Помощь')
keyboard.add(button1, button2)

# Обработчик команды /start
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply(
        "Привет! Я отчето-бот. Отправь мне отчет",
        reply_markup=keyboard
    )

# Обработчик команды /help
@dp.message_handler(commands=['help'])
async def send_help(message: types.Message):
    await message.reply("Я собираю отчеты, которые ты мне отправляешь.")

# Обработчик всех остальных сообщений
@dp.message_handler()
async def echo(message: types.Message):  # Замените на идентификатор чата, куда нужно отправлять сообщения
    user_name = message.from_user.first_name  # Получаем имя пользователя
    await bot.send_message(CHAT_ID, f"{user_name}:\n {message.text}")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True) 