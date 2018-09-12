# from pyramid_restful.viewsets import APIViewSet
from pyramid.response import Response
from pyramid.view import view_config


@view_config(route_name='account', renderer='json', request_method='GET')
def get_view(request):
    """
    This is the authorization route
    """
    message = 'Get accounts route hit!!!!\n'
    
    return Response(body=message, content_type='text/plain', status=200)


@view_config(route_name='account', renderer='json', request_method='POST')
def post_view(request):
    """
    This is the authorization route
    """
    message = 'New account route hit!!!!\n'
    
    return Response(body=message, content_type='text/plain', status=201)


@view_config(route_name='account', renderer='json', request_method='PUT')
def put_view(request):
    """
    This is the authorization route
    """
    message = 'Update account route hit!!!!\n'
    
    return Response(body=message, content_type='text/plain', status=202)


@view_config(route_name='account', renderer='json', request_method='DELETE')
def delete_view(request):
    """
    This is the authorization route
    """
    message = 'Remove account route hit!!!!\n'
    
    return Response(body=message, content_type='text/plain', status=203)


# class AuthAPIView(APIViewSet):
#     def create(self, request, auth=None):
#         """
#         """
#         pass
        # data = json.loads(request.body)

        # if auth == 'register':
        #     try = Account.new(
        #         request,
        #         data['email'],
        #         data['password'])
        #     except (integrityError, KeyError):
        #         return Response(json='Bad Request', status=400)

        #     # TODO: Refactor to use JSON Web Token
        #     return Response(json='Created', status=201)

        # if auth == 'login':
        #     pass

        # return Response(json='Not Found', status=404)
