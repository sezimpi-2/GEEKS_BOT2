import asyncio
import logging
from config import bot,dp,set_menu
#from handlers.picture import picture_router
from handlers.start import start_router
from handlers.echo import echo_router
from handlers.shop import shop_router
from handlers.survey import survey_router

async def main():
    # регистрация обработчиков
    dp.include_router(start_router)
    dp.include_router(survey_router)
    dp.include_router(shop_router)
    dp.include_router(echo_router)

    await set_menu()
    # запуск бота
    await dp.start_polling(bot)
    
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())