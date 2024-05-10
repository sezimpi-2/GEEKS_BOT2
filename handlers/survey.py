from aiogram import Router, F, types
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command
from aiogram.fsm.state import State, StatesGroup

survey_router = Router()
class BookSurvey(StatesGroup):
    name = State() # name - имя пользователя
    age = State() # age - возраст пользователя
    gender = State() # gender - пол пользователя
    genre = State() # genre - любимый жанр литературы


@survey_router.message(Command("opros"))
async def start_survey(message: types.Message,state: FSMContext ):
    current_state = await state.get_state()
    if current_state == "Survey":  # Проверяем, что пользователь находится в состоянии для прохождения опроса
        await state.set_state(BookSurvey.name)
        await message.answer("Как вас зовут?" )
    else:
        await message.answer("Опрос не доступен в данный момент.")
@survey_router.message(BookSurvey.name)
async def process_name(message: types.Message,  state: FSMContext):
    name = message.text
    # await message.answer(f"Спасибо, {name}!")
    await state.set_state(BookSurvey.age)
    await message.answer("Ваш номер телефона?")

@survey_router.message(BookSurvey.age)
async def process_age(message: types.Message):
    age = message.text
    if not age.isdigit():
        await message.answer("Дата ващего посещения нащего заведения:")
        return
    age = int(age)
    if age < 10 or age > 100:
        await message.answer("Как оцениваете качество еды  ")
        return
    await state.set_state(BookSurvey.gender)
    await message.answer("Как оцениваете чистоту заведения?")

@survey_router.message(BookSurvey.gender)
async def process_gender(message: types.Message,  state: FSMContext):
    gender = message.text
    await state.set_state(BookSurvey.genre)
    await message.answer("Дополнительные коментарии?")

@survey_router.message(BookSurvey.genre)
async def process_genre(message: types.Message):
    genre = message.text
    
    await message.answer(f"Спасибо за прохождение опроса, {message.from_user.full_name}!")
    await state.clear()