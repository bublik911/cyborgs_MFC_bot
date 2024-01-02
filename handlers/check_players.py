import prettytable

from aiogram import Router, F
from aiogram.enums.parse_mode import ParseMode
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from DataBase.repositories import PlayerRepository

from misc.constValues import CHECK_PLAYERS_LIST

router = Router()




@router.message(
    F.text == CHECK_PLAYERS_LIST
)
async def check_players_list(message: Message):
    query = PlayerRepository.create_players_list()
    table = prettytable.PrettyTable()
    table.field_names = ["Имя", "Телефон"]
    table.align = 'c'
    for player in query:
        table.add_row([player.name, "+7" + player.phone_number])
    await message.answer(f"```{table}```", parse_mode=ParseMode.MARKDOWN_V2)
