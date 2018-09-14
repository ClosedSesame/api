from pyramid_restful.routers import ViewSetRouter
from .views.auth import AuthAPIView


def includeme(config):
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    
    # This is where user gets authorization.
    router.register('api/v1/auth/{auth}', AuthAPIView, 'auth')