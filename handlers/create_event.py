from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from states import Event

from misc.constValues import ADD_EVENT, TRAINING, GAME

from keyboards.admin_panel import admin_panel_keyboard
from keyboards.event_type import event_type_keyboard
from keyboards.event_place import event_place_keyboard
from keyboards.event_date import day_keyboard

from DataBase.repositories import EventRepository


router = Router()


@router.message(
    F.text == ADD_EVENT
)
async def create_event(message: Message, state: FSMContext):
    await message.answer("Какое событие создаем?",
                         reply_markup=event_type_keyboard())
    await state.set_state(Event.type)


@router.message(
    F.text == TRAINING,
    Event.type
)
async def place_of_event(message: Message, state: FSMContext):
    await state.update_data(type=message.text)
    await message.answer("Где тренируемся?",
                         reply_markup=event_place_keyboard())
    await state.set_state(Event.place)


@router.message(
    F.text == GAME,
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
    await message.answer("Событие добавлено. Игроки получат уведомление о событии за двое суток\n")
    await EventRepository.create_event(state)
    await message.answer("Что-то еще?",
                         reply_markup=admin_panel_keyboard())

