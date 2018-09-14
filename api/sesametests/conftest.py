import pytest
# import transaction
from ..models.meta import Base
from ..models import get_tm_session


@pytest.fixture(scope='session')
def testapp(request):
    """Function for setting up a test server/app
    """
    from webtest import TestApp
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

    def main():
        """ This function returns a Pyramid WSGI application.
        """
        settings = {
            'sqlalchemy.url': 'postgresql://localhost:5432/closedsesame'
        }

        config = Configurator(settings=settings)
        config.include('pyramid_restful')
        config.include('api.models')
        config.include('pyramid_jwt')

        config.set_root_factory(RootACL)
        config.set_authorization_policy(ACLAuthorizationPolicy())
        config.set_jwt_authentication_policy(
            'supersekrit',
            auth_type='Bearer',
            callback=add_role_principals,
        )
        config.include('api.routes')
        config.scan()
        return config.make_wsgi_app()

    app = main()

    SessionFactory = app.registry['dbsession_factory']
    session = SessionFactory()
    engine = session.bind
    Base.metadata.create_all(bind=engine)

    def tear_down():
        Base.metadata.drop_all(bind=engine)

    request.addfinalizer(tear_down)

    return TestApp(app)
