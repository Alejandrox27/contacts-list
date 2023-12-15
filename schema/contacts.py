from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String

from db.database import engine, meta_data

contacts = Table("contacts", meta_data,
                 Column("id", Integer, primary_key=True),
                 Column("name", String(20), nullable=False),
                 Column("email", String(35), nullable=False),
                 Column("phone", Integer, nullable=False)
                 )

meta_data.create_all(engine)