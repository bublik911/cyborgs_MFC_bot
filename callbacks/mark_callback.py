from aiogram.filters.callback_data import CallbackData


class MarkCallbackFactory(CallbackData, prefix="event"):
    event_id: int
    status: int
