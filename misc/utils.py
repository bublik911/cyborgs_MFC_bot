import datetime

from aiogram import Bot

from keyboards.answer import answer_yes_no

from DataBase.models.EventModel import Event
from DataBase.repositories import PlayerRepository, EventRepository, MarkRepository

from misc.constValues import WEEKDAYS, FIRST_DIVISION


def create_message_for_chat(event: Event) -> str:
    message = ("Всем привет!\n"
               f"{event.type_of_event}, {event.place}\n"
               f"{convert_date_to_weekday(event.date)} в {str(event.time)[:5]}\n"
               f"Сегодня будут:\n")
    return message


def create_message_for_notification(event: Event) -> str:
    message = ("Привет!\n"
               f"{event.type_of_event}, {event.place}\n"
               f"{convert_date_to_weekday(event.date)} в {str(event.time)[:5]}\n"
               f"Ты будешь?")
    return message


def create_message_for_reminder(event: Event) -> str:
    message = ("Привет!\n"
               f"{event.type_of_event}, {event.place}\n"
               f"{convert_date_to_weekday(event.date)} в {str(event.time)[:5]}\n"
               f"Через 3 часа!")
    return message


def convert_date_to_weekday(date: datetime.date) -> str:
    day_number = date.weekday()
    return WEEKDAYS[day_number]


def create_names_list(event_id: int) -> [str]:
    players_id = MarkRepository.get_mark_by_event_id_and_status(event_id)
    names = []
    for pl_id in players_id:
        name = PlayerRepository.get_player_name_by_id(pl_id.player_id)
        names.append(name)
    return names


async def notification_for_chatbot(bot: Bot):
    await players_polling(bot)
    await reminder(bot)


async def reminder(bot: Bot):
    hour = datetime.datetime.now().time().hour
    day = datetime.datetime.now().date().day
    today_events = EventRepository.get_today_events()
    first_division_event = False
    second_division_event = False
    for event in today_events:
        if event.place == FIRST_DIVISION:
            first_division_event = True
        else:
            second_division_event = True

    for event in today_events:
        if event.send is not None and event.time.hour - hour == 3 and event.date.day == day:
            message = create_message_for_reminder(event)

            if not first_division_event and second_division_event and event.type_of_event == "Тренировка":
                players = PlayerRepository.get_all_players()
            else:
                players = PlayerRepository.get_player_by_place(event.place)
            for player in players:
                await bot.send_message(player.chat_id, message)
            EventRepository.update_event_completed(event.id)


async def players_polling(bot: Bot):
    hour = datetime.datetime.now().time().hour
    day = datetime.datetime.now().date().day
    tomorrow_events = EventRepository.get_tomorrow_events()
    first_division_event = False
    second_division_event = False
    for event in tomorrow_events:
        if event.place == FIRST_DIVISION:
            first_division_event = True
        else:
            second_division_event = True

    for event in tomorrow_events:
        if event.send is None and event.date.day - day == 1 and event.time.hour - hour < 12:
            message = create_message_for_notification(event)
            if not first_division_event and second_division_event and event.type_of_event == "Тренировка":
                players = PlayerRepository.get_all_players()
            else:
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
