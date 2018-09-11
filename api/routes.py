from pyramid_restful.routers import ViewSetRouter
# from .views.auth import AuthAPIView

def includeme(config):
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('auth', '/api/v1/auth/')
    # test http post localhost:6543/api/v1/auth/

    # config.add_route('login', '/api/v1/login/')
    # config.add_route('accounts', '/api/v1/accounts/')
    # config.add_route('new_account', '/api/v1/new_account/')
    # config.add_route('update', '/api/v1/update/')
    # config.add_route('remove', '/api/v1/remove/')

    router = ViewSetRouter(config)