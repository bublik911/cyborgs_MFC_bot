import datetime
from keyboards.admin_panel import admin_panel_keyboard
from aiogram import Router, F
from DataBase.models_db import *
from aiogram.types import Message
from keyboards.event_type import event_type_keyboard
from keyboards.event_place import event_place_keyboard
from keyboards.event_date import day_keyboard
from aiogram.fsm.context import FSMContext
from states import Event, Start


router = Router()


@router.message(
    F.text == "Создать событие"
)
async def create_event(message: Message, state: FSMContext):
    await message.answer("Какое событие создаем?",
                         reply_markup=event_type_keyboard())
    await state.set_state(Event.type)


@router.message(
    F.text == "Тренировка",
    Event.type
)
async def place_of_event(message: Message, state: FSMContext):
    await state.update_data(type=message.text)
    await message.answer("Где тренируемся?",
                         reply_markup=event_place_keyboard())
    await state.set_state(Event.place)


@router.message(
    F.text == "Матч",
    Event.type
)
async def place_of_event(message: Message, state: FSMContext):
    await state.update_data(type=message.text)
    await message.answer("Где играем?",
                         reply_markup=event_place_keyboard())
    await state.set_state(Event.place)


@router.message(
    Event.place
)
async def day_of_event(message: Message, state: FSMContext):
    await state.update_data(place=message.text)
    await message.answer("В какой день?",
                         reply_markup=day_keyboard())
    await state.set_state(Event.time)


@router.message(
    Event.time
)
async def time_of_event(message: Message, state: FSMContext):
    await state.update_data(day=message.text)
    await message.answer("Вo сколько? (Формат: часы:минуты)")
    await state.set_state(Event.finish)


@router.message(
    Event.finish
)
async def commit_event(message: Message, state: FSMContext):
    await state.update_data(time=message.text)
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
    # try:
    Events.create(type_of_event=event['type'],
                 place=event['place'],
                 date=datetime.date(year, month, day),
                 time=datetime.time(int(h), int(m))
                  )

    await state.clear()
    # except:
    #     await message.answer("Error")
    await message.answer("Событие добавлено. Игроки получат уведомление о событии за двое суток\n"
                         "Что-то еще?",
                         reply_markup=admin_panel_keyboard())

