import datetime
from keyboards.answer import answer_yes_no
from aiogram import Bot
from DataBase.models_db import *


def phone_parse(x) -> str:
    s = str(x)
    phone = ''
    for i in s:
        if i.isdigit():
            phone += i
    phone = phone[-10:]
    return phone


async def notification_for_chatbot(bot: Bot):
    events_table = Events.select().where(Events.completed.is_null())
    hour = datetime.datetime.now().time().hour
    day = datetime.datetime.now().date().day
    for event in events_table:
        if event.send is not(None) and int(str(event.time).split(":")[0]) - hour == 3 and int(str(event.date).split("-")[2]) == day:
            message = ("Привет!\n"
                       f"{event.type}, {event.place}\n"
                       f"{event.date} в {event.time}\n"
                       f"Через 3 часа!")
            Events.update(completed=1).where(Events.id == event.id).execute()
            players = Player.select().where((Player.place == event.place) & (Player.chat_id.is_null(False)))
            for player in players:
                await bot.send_message(player.chat_id, message)
        if event.send is None and int(str(event.date).split("-")[2]) - day == 1 and int(str(event.time).split(":")[0]) - hour < 12:
            message = ("Привет!\n"
                       f"{event.type_of_event}, {event.place}\n"
                       f"{event.date} в {event.time}\n"
                       f"Ты будешь?")

            players = Player.select().where((Player.place == event.place) & (Player.chat_id.is_null(False)))
            for player in players:
                pId = player.id
                eId = event.id
                Mark.create(event_id=eId,
                            player_id=pId)
                await bot.send_message(player.chat_id, message,
                                       reply_markup=answer_yes_no(event.id))
            Events.update(send=1).where(Events.id == event.id).execute()




