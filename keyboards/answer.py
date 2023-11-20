from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardMarkup
from callbacks.mark_callback import MarkCallbackFactory


def answer_yes_no(id: int) -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardBuilder()
    keyboard.button(text="Я пойду", callback_data=MarkCallbackFactory(event_id=id, status=1))
    keyboard.button(text="Я не пойду", callback_data=MarkCallbackFactory(event_id=id, status=0))
    return keyboard.as_markup()
