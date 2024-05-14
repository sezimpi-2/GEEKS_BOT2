from aiogram import Router, F, types
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command
from aiogram.fsm.state import State, StatesGroup


survey_router = Router()

class PizzaSurvey(StatesGroup):
    name = State()  # имя пользователя
    age = State()  # возраст пользователя
    gender = State()  # пол пользователя
    genre = State()  # любимый жанр литературы
    feedback = State()  # отзыв о пиццерии

@survey_router.message(Command("opros"))
async def start_survey(message: types.Message, state: FSMContext):
    await PizzaSurvey.name.set()
    await message.answer("Привет! Как тебя зовут?")

@survey_router.message()
async def process_name(message: types.Message, state: FSMContext):
    name = message.text
    await state.update_data(name=name)
    await PizzaSurvey.age.set()
    await message.answer("Сколько тебе лет?")

@survey_router.message()
async def process_age(message: types.Message, state: FSMContext):
    age = message.text
    if not age.isdigit():
        await message.answer("Пожалуйста, введите ваш возраст цифрами.")
        return

    age = int(age)
    if age < 10 or age > 100:
        await message.answer("Ваш возраст вне допустимого диапазона. Как оцениваете качество еды?")
        await PizzaSurvey.gender.set()
    else:
        await state.update_data(age=age)
        await message.answer("Пожалуйста, введите ваш номер телефона.")

@survey_router.message()
async def process_gender(message: types.Message, state: FSMContext):
    gender = message.text
    await state.update_data(gender=gender)
    await PizzaSurvey.genre.set()
    await message.answer("Как оцениваете чистоту заведения?")

@survey_router.message()
async def process_genre(message: types.Message, state: FSMContext):
    genre = message.text
    await state.update_data(genre=genre)
    await PizzaSurvey.feedback.set()
    await message.answer("Пожалуйста, оставьте дополнительные комментарии.")

@survey_router.message()
async def process_feedback(message: types.Message, state: FSMContext):
    feedback = message.text
    await state.update_data(feedback=feedback)
    await message.answer("Спасибо за прохождение опроса!")

    # Здесь можно получить данные из состояния и сохранить их в базу данных или другое хранилище
    survey_data = await state.get_data()
    # Пример сохранения в базу данных:
    # save_to_database(survey_data)

    # Очистка состояния
    await state.finish()
