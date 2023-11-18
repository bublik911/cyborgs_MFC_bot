from aiogram.utils.keyboard import ReplyKeyboardBuilder, ReplyKeyboardMarkup


def event_place_keyboard() -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardBuilder()
    keyboard.button(text="Манеж")
    keyboard.button(text="ИАТЭ")
    return keyboard.as_markup(
        one_time_keyboard=True,
        resize_keyboard=True
    )
