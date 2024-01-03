from peewee import *

from DataBase.config import db


class Player(Model):
    id = AutoField()
    name = CharField()
    phone_number = CharField()
    chat_id = CharField(null=True)
    status = IntegerField()
    place = CharField()
    deleted_at = DateField(null=True)

    class Meta:
        db_table = 'player'
        database = db


Player.create_table()
