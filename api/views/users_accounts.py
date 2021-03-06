from sqlalchemy.exc import IntegrityError, DataError
from pyramid_restful.viewsets import APIViewSet
from pyramid.response import Response
import requests
import json
import os
from ..models.users import Users
from ..models.user_accounts import UserAccounts
from ..models.schemas import UserAccountsSchema


class UserAccountsAPIView(APIViewSet):
    def create(self, request):
        """
        """
        try:
            kwargs = json.loads(request.body)
        except json.JSONDecodeError as e:
            return Response(json=e.msg, status=400)

        if 'website' not in kwargs:
            return Response(json='Expected value; website')
        if 'user_name' not in kwargs:
            return Response(json='Expected value; user name')
        if 'password' not in kwargs:
            return Response(json='Expected value; password')

        try:
            user = Users.new(request=request, **kwargs)
        except IntegrityError:
            return Response(json='Bad Request', status=400)

        schema = UserAccountsSchema()
        data = schema.dump(user).data

        return Response(json=data, status=201)

    def list(self, request):
        """
        """
        records = UserAccounts.all(request)
        schema = UserAccountsSchema()
        data = [schema.dump(record).data for record in records]

        return Response(json=data, status=200)

    def retrieve(self, request, id=None):
        """
        """
        record = UserAccounts.one(request=request, pk=id)
        if not record:
            return Response(json='No Found', status=400)

        schema = UserAccountsSchema()
        data = schema.dump(record).data

        return Response(json=data, status=200)

    def destroy(self, request, id=None):
        """
        """
        if not id:
            return Response(json='Bad Request', status=400)

        try:
            UserAccounts.remove(request=request, pk=id)
        except (DataError, AttributeError):
            return Response(json='Not Found', status=404)

        return Response(status=204)
