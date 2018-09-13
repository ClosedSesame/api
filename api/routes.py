
from pyramid_restful.routers import ViewSetRouter
from .views.users import AuthAPIView

def includeme(config):
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    # config.add_route('auth', '/api/v1/auth/')
    # test http post localhost:6543/api/v1/auth/
    config.add_route('login', '/api/v1/login/')
    config.add_route('account', '/api/v1/account/')

    router = ViewSetRouter(config, trailing_slash=False)

# TODO: Write views for each route
    # router.register('api/v1/signup', SignUpAPIView, 'signup')
    router.register('api/v1/auth/{auth}', AuthAPIView, 'auth')
#     router.register('api/v1/accounts', AccountsAPIView, 'accounts')
#     router.register('api/v1/new_account', NewAccountAPIView, 'new_account')
#     router.register('api/v1/update', UpdateAPIView, 'update')
#     router.register('api/v1/delete', DeleteAPIView, 'delete')
