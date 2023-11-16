from peewee import *
from playhouse.pool import PooledMySQLDatabase

db = PooledMySQLDatabase(
    host='127.0.0.1',
    user='user',
    password='Root767!',
    database='mk',
    timeout=0,
    charset='utf8mb4'
)


class Player(Model):
    id = AutoField()
    name = CharField()
    phone_number = CharField()
    chat_id = CharField()
    status = IntegerField()

    class Meta:
        db_table = 'consultants'
        database = db


Player.create_table()