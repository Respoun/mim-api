from sqlalchemy import Column, Table
from sqlalchemy.sql.sqltypes import Integer, String
from app.config.db import meta, engine

quests = Table(
    "quest",
    meta,
    Column("id", Integer, primary_key=True),
    Column("title",String(45)),
)

meta.create_all(engine)