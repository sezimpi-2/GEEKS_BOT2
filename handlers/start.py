from aiogram import Router, F, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext


start_router = Router()

# Создаем объект хранилища состояний


# Обработчики
@start_router.message(Command("start"))
async def start_cmd(message: types.Message, state: FSMContext):
    kb = types.InlineKeyboardMarkup(inline_keyboard=[
        [
            types.InlineKeyboardButton(text="Наш сайт", url="https://pizza.kg"),
            types.InlineKeyboardButton(text="Наш инстаграм", url="https://instagram.com/pizza.kg")
        ],
        [
            types.InlineKeyboardButton(text="О нас", callback_data="about_us")
        ],
        [types.InlineKeyboardButton(text="Оставить отзыв", callback_data="leave_feedback")],
    ])

    await message.answer(f"Привет, {message.from_user.first_name}", reply_markup=kb)

    # Проверяем состояние пользователя
    async with state.proxy() as data:
        if "state" in data and data["state"] == "Feedback":
            await message.answer("Проходите опрос")
            await state.set_state(None)  # Очищаем состояние

@start_router.callback_query(lambda c: c.data == "about_us") 
async def about_us(callback: types.CallbackQuery):
    await callback.answer()
    await callback.message.answer("О нас")


