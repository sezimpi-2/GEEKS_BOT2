from aiogram import Router, F, types
from aiogram.filters import Command


menu_router = Router()


@menu_router.message(Command("menu"))
async def show_categories(message: types.Message):
    kb = types.ReplyKeyboardMarkup(
        keyboard=[
            [
                types.KeyboardButton(text="Виды пиццы"),
                types.KeyboardButton(text="Напитки")
            ],
            [
                types.KeyboardButton(text="Пеперони и кола"),
            ]
        ],
        resize_keyboard=True
    )
    await message.answer("наше меню:", reply_markup=kb)


@menu_router_router.message(F.text.lower() == "Виды пиццы")
async def show_triller(message: types.Message):
    await message.answer("Пеперони, Чили, Маргарита")


@menu_router.message(F.text.lower() == "Напитки")
async def show_triller(message: types.Message):
    await message.answer("Напитки:кола, пепси, фанта")