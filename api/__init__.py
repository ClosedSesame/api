from pyramid.config import Configurator
from pyramid.authorization import ACLAuthorizationPolicy
from pyramid.security import Allow, ALL_PERMISSIONS


class RootACL(object):
    __acl__ = [
        (Allow, 'member', ALL_PERMISSIONS),

    ]

    def __init__(self, request):
        pass


def add_role_principals(userid, request):
    return request.jwt_claims.get('roles', [])


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    config.include('pyramid_restful')
    config.include('.models')
    config.include('pyramid_jwt')

    config.set_root_factory(RootACL)
    config.set_authorization_policy(ACLAuthorizationPolicy())
    config.set_jwt_authentication_policy(
        'supersekrit',
        auth_type='Bearer',
        callback=add_role_principals,
    )

    config.include('.routes')
    config.scan()
    return config.make_wsgi_app()
