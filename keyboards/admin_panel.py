from aiogram.utils.keyboard import ReplyKeyboardBuilder, ReplyKeyboardMarkup


def admin_panel_keyboard() -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardBuilder()
    keyboard.button(text="Создать событие")
    keyboard.button(text="Добавить игрока")
    return keyboard.as_markup(
        one_time_keyboard=True,
        resize_keyboard=True
    )
