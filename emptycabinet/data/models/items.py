from sqlalchemy import Column, Integer, String

from emptycabinet.data.database import db_init


class Item(db_init.Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, index=True, nullable=False)
