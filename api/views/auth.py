from pyramid_restful.viewsets import APIViewSet
from sqlalchemy.exc import IntegrityError
from pyramid.response import Response
from ..models.account import Account

import json


class AuthAPIView(APIViewSet):
    def create(self, request, auth=None):
        """
        """
        data = json.loads(request.body.decode())
        if auth == 'register':
            try:
                new_account = Account.new(
                    request,
                    email=data['email'],
                    password=data['password'])
            except (IntegrityError, KeyError):
                return Response(json='Bad Request', status=400)

            return Response(
                json_body={
                    'token': request.create_jwt_token(
                        new_account.email,
                        userName=new_account.email,
                    ),
                },
                status=201
            )
        
        if auth == 'login':
            authenticated = Account.check_credentials(request, data['email'], data['password'])

            if authenticated:
                return Response(
                    json_body={
                        'token': request.create_jwt_token(
                            authenticated.email,
                            userName=authenticated.email,
                        ),
                    },
                    status=201
                )
            return Response(json='Not Authorized', status=401)

        return Response(json='Not Found', status=404)
