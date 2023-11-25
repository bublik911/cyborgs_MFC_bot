from aiogram.utils.keyboard import ReplyKeyboardBuilder, ReplyKeyboardMarkup

from misc.constValues import TRAINING, GAME


def event_type_keyboard() -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardBuilder()
    keyboard.button(text=TRAINING)
    keyboard.button(text=GAME)
    return keyboard.as_markup(
        one_time_keyboard=True,
        resize_keyboard=True)
