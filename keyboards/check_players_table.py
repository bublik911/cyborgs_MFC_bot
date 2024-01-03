from aiogram.utils.keyboard import ReplyKeyboardBuilder, ReplyKeyboardMarkup

from misc.constValues import TABLE_IS_CORRECT, DELETE_PLAYER, ADD_PLAYER


def check_players_table_keyboard() -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardBuilder()
    keyboard.button(text=TABLE_IS_CORRECT)
    keyboard.button(text=DELETE_PLAYER)
    keyboard.button(text=ADD_PLAYER)
    return keyboard.as_markup(
        one_time_keyboard=True,
        resize_keyboard=True
    )
