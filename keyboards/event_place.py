from aiogram.utils.keyboard import ReplyKeyboardBuilder, ReplyKeyboardMarkup

from misc.constValues import FIRST_DIVISION, SECOND_DIVISION


def event_place_keyboard() -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardBuilder()
    keyboard.button(text=SECOND_DIVISION)
    keyboard.button(text=FIRST_DIVISION)
    return keyboard.as_markup(
        one_time_keyboard=True,
        resize_keyboard=True)
