from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types import ReplyKeyboardMarkup


def authorization_keyboard() -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardBuilder()
    keyboard.button(text="Авторизоваться", request_contact=True)
    return keyboard.as_markup(resize_keyboard=True,
                              one_time_keyboard=True)