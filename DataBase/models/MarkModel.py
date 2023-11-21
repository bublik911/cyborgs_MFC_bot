from peewee import *

from DataBase.config import db


class Mark(Model):
    id = AutoField()
    event_id = IntegerField()
    player_id = IntegerField()
    status = IntegerField(null=True)

    class Meta:
        db_table = 'mark'
        database = db


Mark.create_table()
