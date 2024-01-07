from DataBase.models.EventModel import Event

import datetime

from dateutil.parser import parse

from aiogram.fsm.context import FSMContext

from typing import NoReturn

from DataBase.utils import connect


@connect
async def create_event(state: FSMContext) -> NoReturn:
    event = await state.get_data()
    day = int(event['day'])

    if day < datetime.date.today().day and datetime.date.today().month != 12:
        month = datetime.date.today().month + 1
        year = datetime.date.today().year

    elif day < datetime.date.today().day and datetime.date.today().month == 12:
        month = 1
        year = datetime.date.today().year + 1

    else:
        month = datetime.date.today().month
        year = datetime.date.today().year

    h, m = parse(event['time']).hour, parse(event['time']).minute
    Event.create(type_of_event=event['type'],
                 place=event['place'],
                 date=datetime.date(year, month, day),
                 time=datetime.time(h, m))
    await state.clear()


@connect
def update_event_completed(event_id) -> NoReturn:
    Event.update(completed=1).where(Event.id == event_id).execute()


@connect
def update_event_send(event_id) -> NoReturn:
    Event.update(send=1).where(Event.id == event_id).execute()


@connect
def get_event_uncompleted() -> [Event]:
    return Event.select().where(Event.completed.is_null())


@connect
def get_event_by_event_id(event_id: int) -> Event:
    return Event.get(Event.id == event_id)


@connect
def get_tomorrow_events():
    date = datetime.date.today() + datetime.timedelta(days=1)
    return Event.select().where(Event.date == date)


@connect
def get_today_events():
    date = datetime.date.today()
    return Event.select().where(Event.date == date)
