from pyramid.response import Response
from pyramid.view import forbidden_view_config, notfound_view_config


@forbidden_view_config()
def forbidden(request):
    return Response(json_body={'message': 'Forbidden Request'}, status=403)


@notfound_view_config(renderer='json')
def notfound_view(request):
    message = '404 Not Found!\n'
    return Response(body=message, content_type='text/plain', status=404)
