from playhouse.migrate import *

from DataBase.config import db
from DataBase.models.PlayerModel import Player

deleted_at = DateField(null=True)

migrator = MySQLMigrator(db)

migrate(
    migrator.add_column('player', 'deleted_at', deleted_at)
)