from playhouse.migrate import *

from peewee import MySQLDatabase

db = MySQLDatabase(
    host='127.0.0.1',
    user='user', #//user
    password='Root767!',
    database='cyborgs',
    charset='utf8mb4')

deleted_at = DateField(null=True)

migrator = MySQLMigrator(db)

migrate(
    migrator.add_column('player', 'deleted_at', deleted_at)
)