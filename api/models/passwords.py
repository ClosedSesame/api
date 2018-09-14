from .meta import Base
from datetime import datetime as dt
from sqlalchemy.exc import DBAPIError
from sqlalchemy.orm import relationship
from .account import Account
from sqlalchemy import (
    Column,
    String,
    Integer,
    Index,
    Text,
    DateTime,
    ForeignKey,
)

class Passwords(Base):
    """
    """
    __tablename__ = 'passwords'
    id = Column(Integer, primary_key=True)
    website = Column(String, nullable=False, unique=True)
    login = Column(String, nullable=False)
    password = Column(String, nullable=False)
    date_created = Column(DateTime, default=dt.now())
    date_updated = Column(DateTime, default=dt.now(), onupdate=dt.now())
    account_id = Column(Integer, ForeignKey('accounts.id'))

    @classmethod
    def new(cls, request, **kwargs):
        if request.dbsession is None:
            raise DBAPIError

        new_account = cls(**kwargs)
        request.dbsession.add(new_account)

        return request.dbsession.query(cls).filter(
            cls.account_id == kwargs['account_id']
        ).filter(
            cls.website == kwargs['website']
        ).one_or_none()

    @classmethod
    def all(cls, request, account_id):
        if request.dbsession is None:
            raise DBAPIError

        return request.dbsession.query(cls).filter(
            cls.account_id == account_id
        )