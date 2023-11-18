from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardMarkup


def answer_yes_no() -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardBuilder()
    keyboard.button(text="Я пойду", callback_data="yes")
    keyboard.button(text="Я не пойду", callback_data="no")
    return keyboard.as_markup()
