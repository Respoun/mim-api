from sqlalchemy import create_engine, MetaData
import os

engine = create_engine("mysql+pymysql://ulx22cmrwgx8dthz:mRqUyxDYzG76k9TF1xG4@b4wdsgjk77puqlgcampo-mysql.services.clever-cloud.com:3306/b4wdsgjk77puqlgcampo")
engine = create_engine(os.environ.get('DB'))

meta = MetaData()
conn = engine.connect()
