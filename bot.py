import logging
import json
import os
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

# Tokenni xavfsizlik uchun shu yerga yozamiz
API_TOKEN = '8666718768:AAGy49HBI-iMhBBM5YVQ5E1k2ruhS22dZU8'
WEB_APP_URL = "https://begimqulov017.github.io/telegram-bot/"

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(types.KeyboardButton("Menyuni ochish 🍕", web_app=types.WebAppInfo(url=WEB_APP_URL)))
    
    await message.answer(f"Xush kelibsiz, {message.from_user.first_name}!\nBuyurtma berish uchun tugmani bosing.", reply_markup=markup)

@dp.message_handler(content_types=['web_app_data'])
async def get_data(message: types.Message):
    data = json.loads(message.web_app_data.data)
    
    items = "\n".join([f"✅ {i['name']} - {i['price']} so'm" for i in data['items']])
    text = f"🔔 Yangi buyurtma!\n\n{items}\n\n💰 Jami: {data['total']} so'm"
    
    await message.answer(text)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
