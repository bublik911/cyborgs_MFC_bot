from keyboards.authorization import authorization_keyboard
from aiogram import Bot
from DataBase.models_db import Player
from states import Start
from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext


bot = Bot(token="6635292265:AAH8uLVCLZ1RD44J_an5AZ6tBIrisJXwjqI")
router = Router()


@router.message(
    Command("start")
)
async def start(message: Message, state: FSMContext):
    await message.answer("Чтобы начать получать сообщения от бота, необходимо авторизоваться.\n",
                         reply_markup=authorization_keyboard())
    await state.set_state(Start.authorization)


@router.message(
    Start.authorization
)
async def authorization(message: Message):
    if Player.select().where(Player.phone_number == message.contact.phone_number).count() == 0:
        await message.answer("Похоже, ты еще не Киборг и тебе пора записаться на тренировку к нам!\n")
    else:
        await message.answer("Отлично! Жди оповещений о тренировках.")
        Player.update(chat_id=message.chat.id).where(Player.phone_number == message.contact.phone_number).execute()
