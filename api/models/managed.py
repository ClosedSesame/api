from .users import Users
from .meta import Base
from datetime import datetime as dt
from sqlalchemy.orm import relationship
# from .associations import roles_association
from sqlalchemy import (
    Column,
    Index,
    Integer,
    String,
    DateTime,
    ForeignKey,
)


class Accounts(Base):
    """Model class for creating User Roles in the application.
       Roles are pre-configured by our initialization script, but can be modified at the database shell level by an admin.
    """
    __tablename__ = 'account_roles'
    id = Column(Integer, primary_key=True)
    website = Column(String, nullable=False, unique=True)
    user = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False, )
    date_created = Column(DateTime, default=dt.now())
    date_updated = Column(DateTime, default=dt.now(), onupdate=dt.now())
    user_id = Column(Integer, ForeignKey('users.id'))

    # name = Column(String(255), nullable=False, unique=True)
    # accounts = relationship('Account', secondary=roles_association, back_populates='roles')

