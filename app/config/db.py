from sqlalchemy import create_engine, MetaData
import os

engine = create_engine(os.environ.get('DB'))

meta = MetaData()
conn = engine.connect()
