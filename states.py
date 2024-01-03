from aiogram.fsm.state import State, StatesGroup


class Start(StatesGroup):
    authorization = State()
    admin = State()


class Event(StatesGroup):
    transition = State()

    type = State()
    place = State()
    date = State()
    time = State()
    finish = State()


class AddPlayer(StatesGroup):
    transition = State()

    name = State()
    phone = State()
    status = State()


class CheckPlayer(StatesGroup):
    transition = State()
    waiting = State()

    division = State()
    delete = State()
    confirm = State()
    number = State()


class Menu(StatesGroup):
    transition = State()
