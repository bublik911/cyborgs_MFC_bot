from aiogram.utils.keyboard import ReplyKeyboardBuilder, ReplyKeyboardMarkup


def admin_panel_keyboard() -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardBuilder()
    keyboard.button(text="Создать событие")
    return keyboard.as_markup(
        one_time_keyboard=True,
        resize_keyboard=True
    )
