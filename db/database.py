from sqlalchemy import create_engine, MetaData

engine = create_engine("mysql+pymysql://root:@localhost:3306/contacts")

meta_data = MetaData()