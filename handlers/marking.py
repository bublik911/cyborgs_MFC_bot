from aiogram import Router, Bot
from aiogram.types import CallbackQuery
from callbacks.mark_callback import MarkCallbackFactory
from DataBase.models_db import *

bot = Bot(token="6635292265:AAH8uLVCLZ1RD44J_an5AZ6tBIrisJXwjqI")
router = Router()


@router.callback_query(
    MarkCallbackFactory.filter()
)
async def marking(callback: CallbackQuery, callback_data: MarkCallbackFactory):
    chat_id = callback.from_user.id
    player_id = Player.get(Player.chat_id == chat_id).id
    if callback_data.status == 1:
        Mark.update(status=1).where((Mark.player_id == player_id) & (Mark.event_id == callback_data.event_id)).execute()
        await bot.send_message(chat_id=chat_id, text="Отлично, ждем тебя!")
        event = Events.get(Events.id == callback_data.event_id)
        players_id = Mark.select().where((Mark.event_id == callback_data.event_id) & (Mark.status == 1))
        names = []
        for pl_id in players_id:
            name = Player.get(Player.id == pl_id.player_id).name
            names.append(name)
        message = ("Всем привет!\n"
                   f"{event.type_of_event}, {event.place}\n"
                   f"{event.date} в {event.time}\n".join(names))
        if event.place == "ИАТЭ":
            await bot.send_message(chat_id=-1001999805953, text=message, message_thread_id=5)
        if event.place == "Манеж":
            await bot.send_message(chat_id=-1001999805953, text=message, message_thread_id=4)
    if callback_data.status == 0:
        Mark.update(status=0).where((Mark.player_id == player_id) & (Mark.event_id == callback_data.event_id)).execute()
        await bot.send_message(chat_id=chat_id, text="Жаль, ждем тебя в следующий раз!")

