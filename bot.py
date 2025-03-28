import pandas as pd
import os
from aiogram import Bot, Dispatcher, types, F
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardMarkup, KeyboardButton


import constants
from db_manager import DatabaseManager
from parser import Parser

bot = Bot(token=constants.TG_TOKEN)
dp = Dispatcher()

db_manager = DatabaseManager()


@dp.message(F.text == "/start")
async def start_handler(message: types.Message):
    kboard = InlineKeyboardBuilder()
    kboard.button(
        text="Загрузить файл",
        callback_data="load_file"
    )
    reply_kb = ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text="Спарсить сайты")]],
        resize_keyboard=True
    )

    await message.answer("Добро пожаловать в бота для парсинга!", reply_markup=reply_kb)
    await message.answer("Выберите действие:", reply_markup=kboard.as_markup())


@dp.callback_query(F.data == "load_file")
async def request_file(call: types.CallbackQuery):
    return await call.message.answer("Прикрепите Excel-файл с сайтами.")


@dp.message(F.document)                                      # TODO add FSMC State
async def handle_document(message: types.Message):
    file_id = message.document.file_id
    file_info = await bot.get_file(file_id)
    file_path = file_info.file_path
    file_name = message.document.file_name

    local_path = f"downloads/{file_name}"
    os.makedirs("downloads", exist_ok=True)
    await bot.download_file(file_path, local_path)

    df = pd.read_excel(local_path)

    if not {'title', 'url', 'xpath'}.issubset(df.columns):
        await message.answer("Некорректный формат файла. Ожидаются столбцы: title, url, xpath.")
        return

    sites = [(row['title'], row['url'], row['xpath']) for _, row in df.iterrows()]
    db_manager.insert_sites(sites)

    await message.answer(f"Данные загружены в БД")


@dp.message(F.text == "Спарсить сайты")
async def parse_sites_handler(message: types.Message):
    parser = Parser()
    avg_price = parser.get_prices()

    if avg_price:
        await message.answer(f"Средняя цена: {avg_price}")
    else:
        await message.answer("Нет данных для парсинга.")
