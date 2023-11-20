from keyboards.authorization import authorization_keyboard
from keyboards.admins import admin_keyboard
from keyboards.admin_panel import admin_panel_keyboard
from DataBase.models_db import Player
from states import Start
from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext


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
async def authorization(message: Message, state: FSMContext):
    try:
        if Player.select().where(Player.phone_number == message.contact.phone_number[-10:]).count() == 0:
            await message.answer("Похоже, ты еще не Киборг и тебе пора записаться на тренировку к нам!\n",
                                 reply_markup=admin_keyboard())
        if Player.get(Player.phone_number == message.contact.phone_number[-10:]).status == 0:
            await message.answer("Отлично! Жди оповещений о тренировках.")
            Player.update(chat_id=message.chat.id).where(Player.phone_number == message.contact.phone_number[-10:]).execute()
            await state.clear()
        if Player.get(Player.phone_number == message.contact.phone_number[-10:]).status == 1:
            Player.update(chat_id=message.chat.id).where(Player.phone_number == message.contact.phone_number[-10:]).execute()
            await message.answer("Выбери, что хочешь сделать",
                                 reply_markup=admin_panel_keyboard())
            await state.set_state(Start.admin)
    except AttributeError:
        await message.answer("Используй кнопку ниже, чтобы поделиться своим номером телефона",
                             reply_markup=authorization_keyboard())

