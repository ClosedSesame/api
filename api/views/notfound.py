from pyramid.view import notfound_view_config
from pyramid.response import Response


@notfound_view_config(renderer='json')
def notfound_view(request):  
    message = '404 Not Found!\n'
    
    return Response(body=message, content_type='text/plain', status=404)
