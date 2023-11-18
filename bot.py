import asyncio
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from handlers import start, create_event
from aiogram import Bot, Dispatcher


async def main():
    bot = Bot(token="6635292265:AAH8uLVCLZ1RD44J_an5AZ6tBIrisJXwjqI")
    dp = Dispatcher()
    dp.include_routers(start.router, create_event.router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
