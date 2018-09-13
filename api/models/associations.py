from sqlalchemy import Table, Column, Integer, ForeignKey
from .meta import metadata


accounts_association = Table(
    'accounts_association',
    metadata,
    Column('account_id', Integer, ForeignKey('users.id')),
    Column('role_id', Integer, ForeignKey('account_roles.id')),

    # Column('user_id', Integer, ForeignKey('users.id')),
    # Column('account_id', Integer, ForeignKey('user_accounts.id')),
)
