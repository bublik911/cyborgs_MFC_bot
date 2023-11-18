from aiogram.utils.keyboard import ReplyKeyboardBuilder, ReplyKeyboardMarkup


def event_type_keyboard() -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardBuilder()
    keyboard.button(text="Тренировка")
    keyboard.button(text="Матч")
    return keyboard.as_markup(
        one_time_keyboard=True,
        resize_keyboard=True
    )
