from marshmallow_sqlalchemy import ModelSchema
from marshmallow_sqlalchemy.fields import fields
from . import UserAccounts, Users


class UserAccountsScheme(ModelSchema):
    
    class Meta:
        model = UserAccounts


class UsersSchema(ModelSchema):
    accounts = fields.Nested(UserAccountsScheme, many=True, exclude=('id', 'date_created', 'date_updated', 'user_id'))

    class Meta:
        model = Users
