import asyncio
import json
import logging
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command

# Token va URL
API_TOKEN = '8666718768:AAGy49HBI-iMhBBM5YVQ5E1k2ruhS22dZU8'
WEB_APP_URL = "https://begimqulov017.github.io/telegram-bot/"

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    markup = types.ReplyKeyboardMarkup(
        keyboard=[
            [types.KeyboardButton(text="Menyuni ochish 🍕", web_app=types.WebAppInfo(url=WEB_APP_URL))]
        ],
        resize_keyboard=True
    )
    await message.answer(f"Xush kelibsiz, {message.from_user.first_name}!\nPastdagi tugma orqali menyuni oching.", reply_markup=markup)

@dp.message(F.content_type == "web_app_data")
async def web_app_data_handler(message: types.Message):
    data = json.loads(message.web_app_data.data)
    
    items_list = ""
    for item in data['items']:
        items_list += f"✅ {item['name']} — {item['price']:,} so'm\n"
    
    res = (f"🔔 **Yangi buyurtma!**\n\n"
           f"{items_list}\n"
           f"💰 **Jami:** {data['total']:,} so'm")
    
    await message.answer(res, parse_mode="Markdown")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
