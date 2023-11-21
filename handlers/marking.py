from aiogram import Router, Bot
from aiogram.types import CallbackQuery

from misc import env
from misc.constValues import FIRST_DIVISION, SECOND_DIVISION
from misc.utils import create_names_list

from callbacks.mark_callback import MarkCallbackFactory

from DataBase.repositories import PlayerRepository, EventRepository, MarkRepository


bot = Bot(token=env.TgKeys.TOKEN)
router = Router()


@router.callback_query(
    MarkCallbackFactory.filter()
)
async def marking(callback: CallbackQuery, callback_data: MarkCallbackFactory):
    status = callback_data.status
    event_id = callback_data.event_id
    chat_id = callback.from_user.id
    player_id = PlayerRepository.get_player_id_by_chat_id(chat_id)

    if status == 1:
        MarkRepository.update_mark_status_yes(player_id, event_id)
        await bot.send_message(chat_id=chat_id, text="Отлично, ждем тебя!")
        event = EventRepository.get_event_by_event_id(event_id)
        names = create_names_list(event_id)
        message = ("Всем привет!\n"
                   f"{event.type_of_event}, {event.place}\n"
                   f"{event.date} в {event.time}"
                   f"\n".join(names))

        if event.place == FIRST_DIVISION:
            await bot.send_message(chat_id=-1001999805953, text=message, message_thread_id=5)
        elif event.place == SECOND_DIVISION:
            await bot.send_message(chat_id=-1001999805953, text=message, message_thread_id=4)

    elif status == 0:
        await bot.send_message(chat_id=chat_id, text="Жаль, ждем тебя в следующий раз!")
        MarkRepository.update_mark_status_no(player_id, event_id)
