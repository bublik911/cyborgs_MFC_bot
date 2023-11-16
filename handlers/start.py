from DataBase.models_db import Player
from states import Start
from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart, Command
from aiogram import F
from aiogram.fsm.context import FSMContext
router = Router()


@router.message(
    CommandStart
)
async def start(message: Message, state: FSMContext):
    await message.answer("Ты не авторизован")
    await  state.set_state(Start.authorization)


@router.message(
    F.text == "Авторизоваться",
    Start.authorization
)
async def authorization(message: Message, state: FSMContext):
    await message.answer("Введи номер телефона")
    await state.set_state(Start.correct)


@router.message(
    Start.correct
)
async def correct(message: Message, state: FSMContext):
    await message.answer("Ожидай сообщений")
