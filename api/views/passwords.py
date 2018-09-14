from pyramid_restful.viewsets import APIViewSet
from sqlalchemy.exc import IntegrityError, DataError
from pyramid.response import Response
from ..models.passwords import Passwords
from ..models.schema import NewPasswordsSchema
from ..models.account import Account

import json

class PasswordsAPIView(APIViewSet):
    def create(self, request):
        """
        """
        try:
            kwargs = json.loads(request.body.decode())
        except json.JSONDecodeError as e:
            return Response(json=e.msg, status=400)

        if 'website' not in kwargs:
            return Response(json='Expected value: website')
        if 'login' not in kwargs:
            return Response(json='Expected value: login name')
        if 'password' not in kwargs:
            return Response(json='Expected value: password')

        if request.authenticated_userid:
            account = Account.one(request, request.authenticated_userid)
            kwargs['account_id'] = account.id

        try:
            new_store = Passwords.new(request=request, **kwargs)
        except IntegrityError:
            return Response(json='Bad Request', status=400)

        schema = NewPasswordsSchema()
        data = schema.dump(new_store).data

        return Response(json=data, status=201)

    def list(self, request):
        """
        """
        account = Account.one(request, request.authenticated_userid)
        # import pdb; pdb.set_trace()
        
        try:
            records = Passwords.all(request, account.id)
        except AttributeError:
            return Response(json='Bad GET request', status=400)

        schema = NewPasswordsSchema()
        data = [schema.dump(record).data for record in records]

        return Response(json=data, status=200)