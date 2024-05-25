from aiogram import Router, F, types
from aiogram.filters import Command


start_router = Router()

# обработчики
@start_router.message(Command("start"))
async def start_cmd(message: types.Message):
    # print(message.from_user)
    kb = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(text="Наш сайт", url="https://pizza.kg"),
                types.InlineKeyboardButton(text="Наш инстаграм", url="https://instagram.com/pizza.kg")
            ],
            [
                types.InlineKeyboardButton(text="О нас", callback_data="about_us")
            ],
            [
                types.InlineKeyboardButton(text="Пожертвуйте нам", callback_data="donate")
            ],
            [
                types.InlineKeyboardButton(text="Ссылки на объявления", callback_data="house.kg")
            ]
        ]
    )
    await message.answer(f"Привет, {message.from_user.first_name}", reply_markup=kb)
    # await message.reply(f"Привет, {message.from_user.first_name}")


@start_router.callback_query(F.data == "about_us") # lambda query: query.data == "about_us"
async def about_us(callback: types.CallbackQuery):
    await callback.answer()
    await callback.message.answer("О нас")


@start_router.callback_query(F.data == "donate") # lambda query: query.data == "about_us"
async def about_us(callback: types.CallbackQuery):
    await callback.answer()
    await callback.message.answer("Мы будем рады любой сумме :)")

@start_router.callback_query(F.data == "house.kg") # lambda query: query.data == "about_us"
async def about_us(callback: types.CallbackQuery):
    await callback.answer()
    await callback.message.answer("House.kg")