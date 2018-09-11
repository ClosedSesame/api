from pyramid_restful.viewsets import APIViewSet
from pyramid.response import Response
from pyramid.view import view_config


@view_config(route_name='auth', renderer='json', request_method='POST')
def auth_view(request):
    """
    This is the authorization route
    """
    message = 'Authorization route hit!!!!\n'
    return Response(body=message, content_type='text/plain', status=201)


class AuthAPIView(APIViewSet):
    def create(self, request, auth=None):
        """
        """
        data = json.loads(request.body)

        if auth == 'register':
            try = Account.new(
                request,
                data['email'],
                data['password'])
            except (integrityError, KeyError):
                return Response(json='Bad Request', status=400)

            # TODO: Refactor to use JSON Web Token
            return Response(json='Created', status=201)

        if auth == 'login':
            pass

        return Response(json='Not Found', status=404)