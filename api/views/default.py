from pyramid.response import Response
from pyramid.view import view_config


@view_config(route_name='home', renderer='json', request_method='GET')
def home_view(request):
    message = '''
        GET / - Base API route\n
        POST /api/v1/signup/ - Register a new account\n
        POST /api/v1/login/ - Login to an existing account\n
        GET /api/v1/accounts/ - Retrieve all weather information\n
        POST /api/v1/new_account - Retrieve specific weather record\n
        PUT /api/v1/update/ - Create new weather record\n
        DELETE /api/v1/delete - Remove existing weather record\n
    '''
    return Response(body=message, content_type='text/plain', status=200)
