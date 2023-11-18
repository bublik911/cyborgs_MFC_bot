import datetime

from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types import ReplyKeyboardMarkup


def day_keyboard() -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardBuilder()
    day = int(str(datetime.date.today()).split("-")[2])
    if 31 - day < 7:
        k = 1
        while day != 32:
            keyboard.button(text=f"{day}")
            day += 1
            k += 1
        day = 1
        while k != 8:
            keyboard.button(text=f"{day}")
            day += 1
            k += 1
    else:
        for day in range(day, day + 7):
            keyboard.button(text=f"{day}")
    keyboard.adjust(7)
    return keyboard.as_markup(resize_keyboard=True,
                              one_time_keyboard=True)
