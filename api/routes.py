from pyramid_restful.routers import ViewSetRouter
from .views.auth import AuthAPIView
from .views.passwords import PasswordsAPIView


def includeme(config):
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')

    router = ViewSetRouter(config, trailing_slash=False)
    
    # This is where user gets authorization.
    router.register('api/v1/auth/{auth}', AuthAPIView, 'auth')
    router.register('api/v1/passwords', PasswordsAPIView, 'passwords')