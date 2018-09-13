from pyramid_restful.viewsets import APIViewSet
from sqlalchemy.exc import IntegrityError
from pyramid.response import Response
from ..models.users import Users
import json


class AuthAPIView(APIViewSet):
    def create(self, request, auth=None):
        """
        """
        print('this is the request', request)
        data = json.loads(request.body.decode())
        print(data)
        if auth == 'register':
            try:
                account = Users.new(
                    request,
                    email=data['email'],
                    password=data['password'])
            except (IntegrityError, KeyError):
                return Response(json='Bad Request', status=400)

            # NOTE: Refactored this for authentication / JSON Web Token
            return Response(
                json_body={
                    'token': request.create_jwt_token(
                        account.email,
                        userName=account.email,
                    ),
                },
                status=201
            )

        if auth == 'login':
            authenticated = Users.check_credentials(request, data['email'], data['password'])

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
