from sqlalchemy import create_engine, MetaData
import os

URI = os.environ['DB']
engine = create_engine(URI)

meta = MetaData()
conn = engine.connect()
