from aiogram.utils.keyboard import ReplyKeyboardBuilder, ReplyKeyboardMarkup

from misc.constValues import CHECK_PLAYERS_LIST, ADD_PLAYER, ADD_EVENT


def admin_panel_keyboard() -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardBuilder()
    keyboard.button(text=ADD_EVENT)
    keyboard.button(text=ADD_PLAYER)
    keyboard.button(text=CHECK_PLAYERS_LIST)
    return keyboard.as_markup(
        one_time_keyboard=True,
        resize_keyboard=True
    )
