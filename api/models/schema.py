from marshmallow_sqlalchemy import ModelSchema
from marshmallow_sqlalchemy.fields import fields
from .account import Account
from .passwords import Passwords

class NewPasswordsSchema(ModelSchema):
    class Meta:
        model = Passwords