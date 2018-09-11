import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.txt')) as f:
    README = f.read()
with open(os.path.join(here, 'CHANGES.txt')) as f:
    CHANGES = f.read()

requires = [
    'cryptacular',  # Manual
    'marshmallow-sqlalchemy',  # Manual
    'plaster_pastedeploy',
    'psycopg2-binary',  # Manual
    'pyramid >= 1.9a',
    'pyramid_debugtoolbar',
<<<<<<< HEAD
    'pyramid_jinja2',
    'pyramid_jwt',  # Manual
    'pyramid-restful-framework',  # Manual
    'pyramid_retry',
    'pyramid_tm',
    'requests',  # Manual
=======
    'pyramid-restful-framework',  # Custom
    'pyramid_retry',
    'pyramid_tm',
    'requests',  # Custom
>>>>>>> 036f53d50a3c52d617342ec26772a1ef9017ba5e
    'SQLAlchemy',
    'transaction',
    'zope.sqlalchemy',
    'waitress',
]

tests_require = [
    'WebTest >= 1.3.1',  # py3 compat
    'pytest',
    'pytest-cov',
]

setup(
    name='api',
    version='0.0',
    description='closedsesame',
    long_description=README + '\n\n' + CHANGES,
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Pyramid',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Application',
    ],
    author='',
    author_email='',
    url='',
    keywords='web pyramid pylons',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    extras_require={
        'testing': tests_require,
    },
    install_requires=requires,
    entry_points={
        'paste.app_factory': [
            'main = api:main',
        ],
        'console_scripts': [
            'initialize_api_db = api.scripts.initializedb:main',
        ],
    },
)
