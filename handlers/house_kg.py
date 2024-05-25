from aiogram import Router, F, types
from aiogram.filters import Command
import httpx
from parsel import Selector

house_router = Router()

async def parse_ads():
    url = 'https://www.house.kg/snyat'
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        response.raise_for_status()
        selector = Selector(response.text)
        links = selector.css('div.list-item a::attr(href)').getall()
        full_links = ['https://www.house.kg' + link for link in links if link.startswith('/details/')]
        return full_links

@router.message(lambda message: message.text == 'Получить ссылки на объявления')
async def send_links(message: types.Message):
    links = await parse_ads()
    for link in links:
        await message.answer(link)