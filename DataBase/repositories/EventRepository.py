from DataBase.models.EventModel import Event

import datetime

from aiogram.fsm.context import FSMContext

from typing import NoReturn


async def create_event(state: FSMContext) -> NoReturn:
    event = await state.get_data()
    day = int(event['day'])
    if day < int(str(datetime.date.today()).split("-")[2]) and int(str(datetime.date.today()).split("-")[1] != 12):
        month = int(str(datetime.date.today()).split("-")[1]) + 1
        year = int(str(datetime.date.today()).split("-")[0])
    elif day < int(str(datetime.date.today()).split("-")[2]) and int(str(datetime.date.today()).split("-")[1] == 12):
        month = 1
        year = int(str(datetime.date.today()).split("-")[0]) + 1
    else:
        month = int(str(datetime.date.today()).split("-")[1])
        year = int(str(datetime.date.today()).split("-")[0])
    h, m = str(event['time']).split(":")
    Event.create(type_of_event=event['type'],
                 place=event['place'],
                 date=datetime.date(year, month, day),
                 time=datetime.time(int(h), int(m)))
    await state.clear()


def update_event_completed(event_id) -> NoReturn:
    Event.update(completed=1).where(Event.id == event_id).execute()


def update_event_send(event_id) -> NoReturn:
    Event.update(send=1).where(Event.id == event_id).execute()


def get_event_uncompleted() -> [Event]:
    return Event.select().where(Event.completed.is_null())


def get_event_by_event_id(event_id: int) -> Event:
    return Event.get(Event.id == event_id)
