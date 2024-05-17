from aiogram import Router, F, types
from aiogram.filters import Command

shop_router = Router()

@shop_router.message(Command("shop"))
async def show_categories(message: types.Message):
    kb = types.ReplyKeyboardMarkup(
        keyboard=[
            [
                types.KeyboardButton(text="Диаметр-35см"),
                types.KeyboardButton(text="Диаметр-30см")
            ],
            [
                types.KeyboardButton(text="Диаметр-1м"),
            ]
        ],
        resize_keyboard=True
    )
    await message.answer("Виды пиццы по размеру:", reply_markup=kb)

@shop_router.message(F.text.lower() == "диаметр-25см")
async def show_triller(message: types.Message):
    await message.answer("Пиццы с диаметром 25см")
    kb = types.ReplyKeyboardRemove()
    await message.answer("Виды пиццы с диаметром 25см", reply_markup=kb)


@shop_router.message(F.text.lower() == "Диаметр-30см")
async def show_triller(message: types.Message):
    await message.answer("Пиццы с диаметром 30см")
    kb = types.ReplyKeyboardRemove()
    await message.answer("Виды пиццы с диаметром 30см", reply_markup=kb)