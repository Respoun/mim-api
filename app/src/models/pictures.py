from sqlalchemy import Column, Table, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String, Text
from app.config.db import meta, engine

pictures = Table(
    "picture",
    meta,
    Column("id", Integer, primary_key=True),
    Column("id_enigma",Integer, ForeignKey("enigma.id"), nullable=False),
    Column("url", Text),
    Column("order", Integer),
)

meta.create_all(engine)