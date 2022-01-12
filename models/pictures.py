from sqlalchemy import Column, Table, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String, Text
from config.db import meta, engine

pictures = Table(
    "pictures",
    meta,
    Column("id", Integer, primary_key=True),
    Column("id_enigma",Integer, ForeignKey("enigmas.id"), nullable=False),
    Column("url", Text),
    Column("order", Integer),
)

meta.create_all(engine)