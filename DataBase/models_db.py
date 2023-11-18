from peewee import *
from playhouse.pool import PooledMySQLDatabase

db = MySQLDatabase(
    host='localhost',
    user='egor',
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

    class Meta:
        db_table = 'player'
        database = db


class Events(Model):
    id = AutoField()
    type_of_event = CharField()
    place = CharField()
    date = DateField()
    time = TimeField()
    # completed = BooleanField()

    class Meta:
        db_table = 'event'
        database = db


Player.create_table()
Events.create_table()
