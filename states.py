from aiogram.fsm.state import State, StatesGroup


class Start(StatesGroup):
    authorization = State()
    admin = State()


class Event(StatesGroup):
    type = State()
    place = State()
    date = State()
    time = State()
    finish = State()


class AddPlayer(StatesGroup):
    name = State()
    phone = State()
    status = State()
