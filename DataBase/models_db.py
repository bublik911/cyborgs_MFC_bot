from peewee import *
from playhouse.pool import PooledMySQLDatabase

db = MySQLDatabase(
    host='127.0.0.1',
    user='user',
    password='Root767!',
    database='cyborgs',
    charset='utf8mb4'
)
db.connect()


class Player(Model):
    id = AutoField()
    name = CharField()
    phone_number = CharField()
    chat_id = CharField(null=True)
    status = IntegerField()
    place = CharField()

    class Meta:
        db_table = 'player'
        database = db


class Events(Model):
    id = AutoField()
    type_of_event = CharField()
    place = CharField()
    date = DateField()
    time = TimeField()
    send = CharField(null=True)
    completed = CharField(null=True)

    class Meta:
        db_table = 'event'
        database = db


class Mark(Model):
    id = AutoField()
    event_id = IntegerField()
    player_id = IntegerField()
    status = IntegerField(null=True)

    class Meta:
        db_table = 'mark'
        database = db


Player.create_table()
Events.create_table()
Mark.create_table()
