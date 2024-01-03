from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from keyboards.admin_panel import admin_panel_keyboard

from states import Menu

router = Router()


@router.message(
    Command("menu")
)
@router.message(
    Menu.transition
)
async def menu(message: Message, state: FSMContext):
    await state.clear()
    await message.answer("Выбери, что хочешь сделать",
                        reply_markup=admin_panel_keyboard())
