from alembic.command import upgrade
from alembic.config import Config
import os
import inspect
from pathlib import Path


def run_sql_migrations():

    alembic_path = Path('.') / 'alembic.ini'
    migrations_dir = os.path.dirname(os.path.realpath(__file__))
    config = Config(file_=alembic_path)
    config.set_main_option("script_location", migrations_dir)
    upgrade(config, "head")
