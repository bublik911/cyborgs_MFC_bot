import asyncio
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from handlers import start, create_event, marking
from aiogram import Bot, Dispatcher
from misc.utils import notification_for_chatbot


async def main():
    bot = Bot(token="6635292265:AAH8uLVCLZ1RD44J_an5AZ6tBIrisJXwjqI")
    dp = Dispatcher()
    scheduler = AsyncIOScheduler()
    dp.include_routers(start.router, create_event.router, marking.router)
    scheduler.add_job(notification_for_chatbot, "interval", seconds=30, args=(bot,))
    scheduler.start()
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
