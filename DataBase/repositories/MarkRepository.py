from DataBase.models.MarkModel import Mark

from typing import NoReturn

from DataBase.utils import connect


@connect
def create_mark(event_id: int, player_id: int) -> NoReturn:
    Mark.create(event_id=event_id,
                player_id=player_id)


@connect
def update_mark_status_yes(player_id: int, event_id: int) -> NoReturn:
    Mark.update(status=1).where((Mark.player_id == player_id) & (Mark.event_id == event_id)).execute()


@connect
def update_mark_status_no(player_id: int, event_id: int) -> NoReturn:
    Mark.update(status=0).where((Mark.player_id == player_id) & (Mark.event_id == event_id)).execute()


@connect
def get_mark_by_event_id_and_status(event_id: int) -> [Mark]:
    return Mark.select().where((Mark.event_id == event_id) & (Mark.status == 1))


