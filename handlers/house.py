from aiogram import Router, F, types
from crawler.house_kg import get_links

house_router = Router()

async def send_links(callback_query: types.CallbackQuery):
    await callback_query.answer()
    await callback_query.message.answer("Собираю ссылки, подождите немного...")
    links = get_links()
    for link in links:
        await callback_query.message.answer(link)

