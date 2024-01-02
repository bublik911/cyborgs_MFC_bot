from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from keyboards.admin_panel import admin_panel_keyboard

router = Router()


@router.message(
    Command("menu")
)
async def menu(message: Message, state: FSMContext):
    await state.clear()
    await message.answer("Выбери, что хочешь сделать",
                        reply_markup=admin_panel_keyboard())
