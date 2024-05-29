from aiogram import Router, F, types
from aiogram.filters import Command
from config import database
from pprint import pprint

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
    await message.answer("пиццы по размеру:", reply_markup=kb)
type_pizza= ("Диаметр-35см", "Диаметр-30с", "Диаметр-1м")

@shop_router.message(F.text.lower().in_(type_pizza))
async def show_triller(message: types.Message):
   type_pizza = message.text
   print("Пользователь нажал на кнопку", type_pizza)
   data = await database.fetch(
        """SELECT * FROM pizzas
        INNER JOIN types_pizza ON pizzas.type_pizza_id = types_pizza.id 
        WHERE types_pizza.name = ?""", 
        (type_pizza ,) 
   )
   pprint(data) 
   if not data:
        await message.answer("К сожалению, ничего не нашлось")
        return
   kb = types.ReplyKeyboardRemove()
   await message.answer(f"Пиццы вида {type_pizza}", reply_markup=kb)
   await message.answer(f"Пиццы вида {type_pizza}:", reply_markup=kb)
   for pizza in data:
        image = types.FSInputFile(pizza.get("photo"))
        await message.answer_photo(
            photo=image, 
            caption=f"{pizza['name']} - {pizza['author']}\nЦена: {pizza['price']} сом")