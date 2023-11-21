from peewee import *

from DataBase.config import db


class Event(Model):
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


Event.create_table()
