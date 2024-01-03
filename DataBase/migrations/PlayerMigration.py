from playhouse.migrate import *

from DataBase.config import db

deleted_at = DateField(null=True)

migrator = MySQLMigrator(db)

migrate(
    migrator.add_column('player', 'deleted_at', deleted_at)
)