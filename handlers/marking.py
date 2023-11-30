from aiogram import Router, Bot
from aiogram.types import CallbackQuery

from misc import env
from misc.constValues import FIRST_DIVISION, SECOND_DIVISION
from misc.utils import create_names_list, create_message_for_chat

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

        message = create_message_for_chat(event)
        player_names_list = "\n".join(create_names_list(event_id))

        if event.place == FIRST_DIVISION:
            await bot.send_message(chat_id=-1001999805953, text=message + player_names_list, message_thread_id=5)
        elif event.place == SECOND_DIVISION:
            await bot.send_message(chat_id=-1001999805953, text=message + player_names_list, message_thread_id=4)

    elif status == 0:
        await bot.send_message(chat_id=chat_id, text="Жаль, ждем тебя в следующий раз!")
        MarkRepository.update_mark_status_no(player_id, event_id)
