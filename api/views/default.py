from pyramid.response import Response
from pyramid.view import view_config


@view_config(route_name='home', renderer='json', request_method='GET')
def home_view(request):
    """
    This is the default homepage!
    """
    message = 'Hello Password World!!!!'
    return Response(body=message, content_type='text/plain', status=200)
