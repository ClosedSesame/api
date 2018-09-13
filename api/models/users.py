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

# from .user_accounts import UserAccounts
# from .associations import accounts_association

manager = bcrypt.BCRYPTPasswordManager()


class Users(Base):
    __tablename__ = 'users'
    # TODO: Assess need for a 'user_name'?
    id = Column(Integer, primary_key=True)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    accounts = relationship('UserAccounts', backref='users')  # TODO: Reference the table in .managed/associated/schema
    date_created = Column(DateTime, default=dt.now())
    date_updated = Column(DateTime, default=dt.now(), onupdate=dt.now())

    # NOTE: Added account and account_id refs for relationship management
    # account_id = Column(Integer, ForeignKey('user_accounts.id'), nullable=False)

    # TODO: account needs to be correctly associated with the right table.
    #account = relationship('Account', back_populates='location')

    def __init__(self, email, password):
        self.email = email
        # NOTE: Update the password management
        self.password = manager.encode(password, 10)

    @classmethod
    def new(cls, request, email=None, password=None):
        """
        """
        if request.dbsession is None:
            raise DBAPIError

        user = cls(email, password)
        request.dbsession.add(user)

        return request.dbsession.query(cls).filter(
            cls.email == email).one_or_none()

    @classmethod
    def one(cls, request, email=None):
        return request.dbsession.query(cls).filter(
            cls.email == email).one_or_none()

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
