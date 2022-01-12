from sqlalchemy import create_engine, MetaData

engine = create_engine("mysql+pymysql://ulx22cmrwgx8dthz:mRqUyxDYzG76k9TF1xG4@b4wdsgjk77puqlgcampo-mysql.services.clever-cloud.com:3306/b4wdsgjk77puqlgcampo")

meta = MetaData()
conn = engine.connect()
