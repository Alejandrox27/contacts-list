from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String

from db.database import engine, meta_data

contacts = Table("contacts", meta_data,
                 Column("id", Integer, primary_key=True),
                 Column("name", String, nullable=False),
                 Column("email", String, nullable=False),
                 Column("Phone num", Integer, nullable=False)
                 )

meta_data.create_all(engine)