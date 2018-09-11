from .meta import Base
from datetime import datetime as dt
from sqlalchemy.exc import DBAPIError
# from .associations import roles_association
from sqlalchemy import (
    Column,
    Index,
    Integer,
    String,
    DateTime,
    ForeignKey,
)


class UserAccounts(Base):
    """Model class for User Accounts in the application.
       Roles are pre-configured by our initialization script, but can be modified at the database shell level by an admin.
    """
    __tablename__ = 'user_accounts'
    id = Column(Integer, primary_key=True)
    website = Column(String, nullable=False, unique=True)
    user = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False, )
    date_created = Column(DateTime, default=dt.now())
    date_updated = Column(DateTime, default=dt.now(), onupdate=dt.now())
    user_id = Column(Integer, ForeignKey('users.id'))

    # name = Column(String(255), nullable=False, unique=True)
    # accounts = relationship('Account', secondary=roles_association, back_populates='roles')

    @classmethod
    def new(cls, request, **kwargs):
        if request.dbsession is None:
            raise DBAPIError

        # TODO: Request body needs to have Website, Use/Email, and Password
        new_account = cls(**kwargs)
        request.dbsession.add(new_account)

        return request.dbsession.query(cls).filter(
            # TODO: Change zip code to applicable variables.
            cls.user == kwargs['user']).one_or_none()

    @classmethod
    def one(cls, request, pk=None):
        if request.dbsession is None:
            raise DBAPIError

        return request.dbsession.query(cls).get(pk)

    @classmethod
    def all(cls, request):
        if request.dbsession is None:
            raise DBAPIError

        return request.dbsession.query(cls).all()

    @classmethod
    def remove(cls, request, pk=None):
        if request.dbsession is None:
            raise DBAPIError

        return request.dbsession.query(cls).get(pk).delete()


Index('my_account', UserAccounts.user, unique=True, mysql_length=255)
