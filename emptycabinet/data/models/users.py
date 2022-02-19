from sqlalchemy import Column, Integer, String

from emptycabinet.data.database import db_init


class User(db_init.Base):
    __tablename__ = "users"

    id = Column(
        Integer, primary_key=True, index=True, nullable=False, autoincrement=True
    )
    email = Column(String, index=True, nullable=False, unique=True)
    name = Column(String, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
