from sqlalchemy.orm import relationship
from sqlalchemy.exc import DBAPIError
from datetime import datetime as dt
from .meta import Base
from cryptacular import bcrypt
from sqlalchemy import (
    Column,
    String,
    Integer,
    Index,
    Text,
    DateTime,
    ForeignKey,
)

manager = bcrypt.BCRYPTPasswordManager()

class Account(Base):
    __tablename__ = 'accounts'
    id = Column(Integer, primary_key=True)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    role = Column(String, nullable=False, default='member')
    date_created = Column(DateTime, default=dt.now())
    date_updated = Column(DateTime, default=dt.now(), onupdate=dt.now())

    def __init__(self, email, password):
        self.email = email
        self.password = manager.encode(password, 10) # Hashes the password

    @classmethod
    def new(cls, request, email=None, password=None):
        """
        """
        if request is None:
            raise DBAPIError

        account = cls(email, password)
        request.dbsession.add(account)

        return request.dbsession.query(cls).filter(
            cls.email == email
        ).one_or_none()

    @classmethod
    def check_credentials(cls, request=None, email=None, password=None):

        if request.dbsession is None:
            raise DBAPIError

        try:
            query = request.dbsession.query(cls).filter(
                cls.email == email).one_or_none()
                
        except DBAPIError:
            raise DBAPIError

        if query is not None:
            if manager.check(query.password, password):
                return query

        return None
