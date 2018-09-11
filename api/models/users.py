from sqlalchemy.orm import relationship
from sqlalchemy.exc import DBAPIError
from datetime import datetime as dt
from sqlalchemy import (
    Column,
    String,
    Integer,
    Index,
    Text,
    DateTime,
    ForeignKey,
)

from .meta import Base
from .user_accounts import UserAccounts
from .associations import accounts_association


class Users(Base):
    __tablename__ = 'users'
    # TODO: Assess need for a 'user_name'?
    id = Column(Integer, primary_key=True)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    accounts = relationship(UserAccounts, secondary=accounts_association, back_populates='users')  # TODO: Reference the table in .managed/associated/schema
    date_created = Column(DateTime, default=dt.now())
    date_updated = Column(DateTime, default=dt.now(), onupdate=dt.now())

    # NOTE: Added account and account_id refs for relationship management
    account_id = Column(Integer, ForeignKey('user_accounts.id'), nullable=False)

    # TODO: account needs to be correctly associated with the right table.
    #account = relationship('Account', back_populates='location')
