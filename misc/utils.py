import datetime

from dateutil.parser import parse

from aiogram import Bot

from keyboards.answer import answer_yes_no

from DataBase.repositories import PlayerRepository, EventRepository, MarkRepository


def create_names_list(event_id: int) -> [str]:
    players_id = MarkRepository.get_mark_by_event_id_and_status(event_id)
    names = []
    for pl_id in players_id:
        name = PlayerRepository.get_player_name_by_id(pl_id.player_id)
        names.append(name)
    return names


async def notification_for_chatbot(bot: Bot):
    events_table = EventRepository.get_event_uncompleted()
    hour = datetime.datetime.now().time().hour
    day = datetime.datetime.now().date().day
    for event in events_table:
        if event.send is not(None) and event.time.hour - hour == 3 and event.date.day == day:
            message = ("Привет!\n"
                       f"{event.type_of_event}, {event.place}\n"
                       f"{event.date} в {str(event.time)[:5]}\n"
                       f"Через 3 часа!")
            EventRepository.update_event_completed(event.id)
            players = PlayerRepository.get_player_by_place(event.place)
            for player in players:
                await bot.send_message(player.chat_id, message)
        if event.send is None and event.date.day - day == 1 and event.time.hour - hour < 12:
            message = ("Привет!\n"
                       f"{event.type_of_event}, {event.place}\n"
                       f"{event.date} в {str(event.time)[:5]}\n"
                       f"Ты будешь?")

            players = PlayerRepository.get_player_by_place(event.place)
            for player in players:
                await bot.send_message(player.chat_id, message,
                                       reply_markup=answer_yes_no(event.id))
                MarkRepository.create_mark(event.id, player.id)
            EventRepository.update_event_send(event.id)


def phone_parse(x) -> str:
    s = str(x)
    phone = ''
    for i in s:
        if i.isdigit():
            phone += i
    phone = phone[-10:]
    return phone

