from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from states import AddPlayer

from misc.constValues import ADD_PLAYER
from misc.utils import phone_parse

from keyboards.place import place_keyboard
from keyboards.admin_panel import admin_panel_keyboard

from DataBase.repositories import PlayerRepository

router = Router()


@router.message(
    F.text == ADD_PLAYER
)
async def create_player(message: Message, state: FSMContext):
    await message.answer("Введи имя игрока")
    await state.set_state(AddPlayer.name)


@router.message(
    AddPlayer.name
)
async def add_client_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer("Введите номер телефона клиента")
    await state.set_state(AddPlayer.phone)


@router.message(
    AddPlayer.phone
)
async def add_player_phone(message: Message, state: FSMContext):
    await state.update_data(phone=phone_parse(message.text))
    await message.answer("В заявке на какой турнир?",
                         reply_markup=place_keyboard())
    await state.set_state(AddPlayer.status)


@router.message(
    AddPlayer.status
)
async def commit(message: Message, state: FSMContext):
    await state.update_data(status=message.text)
    await message.answer("Игрок добавлен. Чтобы пользоваться ботом, ему нужно авторизоваться")
    await PlayerRepository.create_player(state)
    await message.answer("Что-то еще?",
                         reply_markup=admin_panel_keyboard())
