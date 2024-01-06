import datetime

import prettytable

from aiogram import Router, F
from aiogram.enums.parse_mode import ParseMode
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from DataBase.repositories import PlayerRepository

from keyboards.place import place_keyboard
from keyboards.check_players_table import check_players_table_keyboard

from misc.constValues import CHECK_PLAYERS_LIST, ADD_PLAYER, DELETE_PLAYER, TABLE_IS_CORRECT

from states import CheckPlayer, Menu, AddPlayer

from handlers.menu import menu
from handlers.create_player import create_player

router = Router()


@router.message(
    F.text == CHECK_PLAYERS_LIST
)
async def choose_division(message: Message, state: FSMContext):
    await state.set_state(CheckPlayer.division)
    await message.answer("Список игроков какого дивизиона хотите посмотреть?",
                         reply_markup=place_keyboard())


@router.message(
    CheckPlayer.division
)
async def check_players_list(message: Message, state: FSMContext):
    query = PlayerRepository.create_players_list(message.text)

    await state.update_data(place=message.text)

    table = prettytable.PrettyTable()
    table.field_names = ["№", "Имя", "Телефон"]
    table.align = 'c'
    i = 1
    for player in query:
        table.add_row([i, player.name, "+7" + player.phone_number])
        i += 1
    await message.answer(f"```{table}```", parse_mode=ParseMode.MARKDOWN_V2)

    await state.set_state(CheckPlayer.waiting)
    await message.answer("Все верно?",
                         reply_markup=check_players_table_keyboard())


@router.message(
    CheckPlayer.waiting
)
async def answer_routing(message: Message, state: FSMContext):
    if message.text == DELETE_PLAYER:
        await state.set_state(CheckPlayer.delete)
        await number_for_delete_player(message, state)
    elif message.text == TABLE_IS_CORRECT:
        await state.set_state(Menu.transition)
        await menu(message, state)
    elif message.text == ADD_PLAYER:
        await state.set_state(AddPlayer.transition)
        await create_player(message, state)


@router.message(
    CheckPlayer.delete
)
async def number_for_delete_player(message: Message, state: FSMContext):
    await message.answer("Введите номер игрока в таблице для удаления")
    await state.set_state(CheckPlayer.number)


@router.message(
    CheckPlayer.number
)
async def delete_confirm(message: Message, state: FSMContext):
    number = message.text
    data = await state.get_data()
    query = PlayerRepository.create_players_list(data['place'])
    i = 1
    for player in query:
        if int(number) == i:
            phone_number = player.phone_number
            id = PlayerRepository.get_id_by_phone_number(phone_number)
            await message.answer(f"Игрок {player.name} удален")
            PlayerRepository.delete_player_by_id(id)
            break
        i += 1
    await state.set_state(Menu.transition)
    await menu(message, state)
