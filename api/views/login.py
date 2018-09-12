# from pyramid_restful.viewsets import APIViewSet
from pyramid.response import Response
from pyramid.view import view_config


@view_config(route_name='login', renderer='json', request_method='POST')
def home_view(request):
    """
    This is the authorization route
    """
    message = 'Login route hit!!!!\n'
    
    return Response(body=message, content_type='text/plain', status=201)
