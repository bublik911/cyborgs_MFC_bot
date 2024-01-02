import asyncio

from aiogram import Bot, Dispatcher

from apscheduler.schedulers.asyncio import AsyncIOScheduler

from handlers import start, create_event, marking, create_player, menu, check_players

from misc import env
from misc.utils import notification_for_chatbot


async def main():
    bot = Bot(token=env.TgKeys.TOKEN)
    dp = Dispatcher()
    scheduler = AsyncIOScheduler()
    dp.include_routers(start.router, menu.router, create_event.router, marking.router, create_player.router, check_players.router)
    scheduler.add_job(notification_for_chatbot, "interval", seconds=3600, args=(bot,))
    scheduler.start()
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
