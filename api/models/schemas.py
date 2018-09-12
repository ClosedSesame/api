from marshmallow_sqlalchemy import ModelSchema
from marshmallow_sqlalchemy.fields import fields
from .users import Users
from .user_accounts import UserAccounts


class UserAccountsSchema(ModelSchema):

    class Meta:
        model = UserAccounts


class UsersSchema(ModelSchema):
    accounts = fields.Nested(UserAccountsScheme, many=True, exclude=('id', 'date_created', 'date_updated', 'user_id'))

    class Meta:
        model = Users
