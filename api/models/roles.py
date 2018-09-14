from .meta import Base
from sqlalchemy.orm import relationship
from .associations import accounts_association
from sqlalchemy import (
    Column,
    Index,
    Integer,
    String,
)


class AccountRole(Base):
    """Model class for creating User Roles in the application.
       Roles are pre-configured by our initialization script, but can be modified at the database shell level by an admin.
    """
    __tablename__ = 'account_roles'
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False, unique=True)
    users = relationship('Users', secondary=accounts_association, back_populates='roles')