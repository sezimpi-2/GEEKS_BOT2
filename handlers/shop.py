from aiogram import Router, F, types
from aiogram.filters import Command


shop_router = Router()


@shop_router.message(Command("shop"))
async def show_categories(message: types.Message):
    kb = types.ReplyKeyboardMarkup(
        keyboard=[
            [
                types.KeyboardButton(text="пиццы"),
                types.KeyboardButton(text="напитки")
            ],
            [
                types.KeyboardButton(text="маргарита"),
            ]
        ],
        resize_keyboard=True
    )
    await message.answer("меню:", reply_markup=kb)


@shop_router.message(F.text.lower() == "чили")
async def show_triller(message: types.Message):
    kb = types.ReplyKeyboardRemove()
    await message.answer("пицца маргарита", reply_markup=kb)


@shop_router.message(F.text.lower() == "чили")
async def show_triller(message: types.Message):
    kb = types.ReplyKeyboardRemove()
    await message.answer("пицца чили", reply_markup=kb)