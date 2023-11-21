from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from states import Start

from keyboards.authorization import authorization_keyboard
from keyboards.admins import admin_keyboard
from keyboards.admin_panel import admin_panel_keyboard

from DataBase.repositories import PlayerRepository

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
        if PlayerRepository.count_player_by_phone_number(message) == 0:
            await message.answer("Похоже, ты еще не Киборг и тебе пора записаться на тренировку к нам!\n",
                                 reply_markup=admin_keyboard())
        elif PlayerRepository.get_player_status_by_phone_number(message) == 0:
            await message.answer("Отлично! Жди оповещений о тренировках.")
            await state.clear()
            PlayerRepository.update_player_chat_id_by_phone_number(message)
        elif PlayerRepository.get_player_status_by_phone_number(message) == 1:
            await message.answer("Выбери, что хочешь сделать",
                                 reply_markup=admin_panel_keyboard())
            await state.set_state(Start.admin)
            PlayerRepository.update_player_chat_id_by_phone_number(message)
    except AttributeError:
        await message.answer("Используй кнопку ниже, чтобы поделиться своим номером телефона",
                             reply_markup=authorization_keyboard())

