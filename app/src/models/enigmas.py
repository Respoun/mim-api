from sqlalchemy import Column, Table, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String, Text
from app.config.db import meta, engine

enigmas = Table(
    "enigma",
    meta,
    Column("id", Integer, primary_key=True),
    Column("id_quest",Integer, ForeignKey("quest.id"), nullable=False),
    Column("title", String(45)),
    Column("id_previous", Integer),
    Column("id_next", Integer),
    Column("content", Text),
    Column("response", Text),
    Column("indice", Text),
)

meta.create_all(engine)