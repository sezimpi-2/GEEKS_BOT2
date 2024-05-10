from aiogram import Router, F, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext


start_router = Router()

# обработчики
@start_router.message(Command("start"))
async def start_cmd(message: types.Message,state: FSMContext ):
    kb = types.InlineKeyboardMarkup(inline_keyboard=[
            [
                types.InlineKeyboardButton(text="Наш сайт", url="https://pizza.kg"),
                types.InlineKeyboardButton(text="Наш инстаграм", url="https://instagram.com/pizza.kg")
            ],
            [
                types.InlineKeyboardButton(text="О нас", callback_data="about_us")
            ],
            [    types.InlineKeyboardButton(text="Оставить отзыв", callback_data="leave_feedback")
            ],
           
        ])
    await message.answer(f"Привет, {message.from_user.first_name}", reply_markup=kb)

    # Проверяем состояние пользователя
    current_state = await state.get_state()
    if current_state == "Feedback":
        await message.answer("Проходите опрос")
        await state.set_state("Survey")

    
@start_router.callback_query(F.data == "about_us") # lambda query: query.data == "about_us"
async def about_us(callback: types.CallbackQuery):
    await callback.answer()
    await callback.message.answer("О нас")


# @start_router.callback_query(F.data == "donate") # lambda query: query.data == "about_us"
# async def about_us(callback: types.CallbackQuery):
#     await callback.answer()
#     await callback.message.answer("Мы будем рады любой сумме :)")