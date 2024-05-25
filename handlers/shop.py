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
    await message.answer("пиццы по размеру:", reply_markup=kb)
types_pizza= ("Диаметр-35см", "Диаметр-30с", "Диаметр-1м")


@shop_router.message(F.text.lower().in_(types_pizza))
async def show_triller(message: types.Message):
   types_pizza = message.text
   print("Пользователь нажал на кнопку", types_pizza)
   data = await database.fetch(
        """SELECT * FROM pizzas 
        INNER JOIN types_pizza ON pizzas.type_pizza_id = types_pizza.id 
        WHERE types_pizza.name = ?""", 
        (types_pizza,)
   )
    print(data)
    if not data:
        await message.answer("К сожалению, ничего не нашлось")
        return
    kb = types.ReplyKeyboardRemove()
    await message.answer(f"Пиццы {types_pizza}", reply_markup=kb)
    await message.answer(f"Пиццы {types_pizza}:", reply_markup=kb)
    for types_pizza in data:
        image = types.FSInputFile(types_pizza.get("picture"))
        await message.answer_photo(
            photo=image, 
            caption=f"{types_pizza['name']} - {types_pizza['author']}\nЦена: {types_pizza['price']} сом")