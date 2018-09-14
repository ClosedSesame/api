import json


def test_registration(testapp):
    """
    """
    account = {
        'email': 'please@work.com',
        'password': 'halo',
    }

    response = testapp.post('/api/v1/auth/register', json.dumps(account))
    assert response.status_code == 201
    assert response.json['token']


def test_invalid_registration(testapp):
    """
    """
    account = {
        'email': 'milly@vanilli.com',
    }

    response = testapp.post('/api/v1/auth/register', json.dumps(account), status='4**')
    assert response.status_code == 400


def test_login(testapp):
    """
    """
    account = {
        'email': 'please@work.com',
        'password': 'halo',
    }

    response = testapp.post('/api/v1/auth/login', json.dumps(account))
    assert response.status_code == 201
    assert response.json['token']


def test_no_passwords_when_empty(testapp):
    """
    """
    response = testapp.get('/api/v1/passwords', status='4**')
    assert response.status_code == 400


def test_no_passwords_when_passing_invalid_account(testapp):
    """
    """
    account = {
        'email': 'milly@vanilli.com',
    }
    response = testapp.get('/api/v1/passwords', json.dumps(account), status='4**')
    assert response.status_code == 400


def test_can_authenticate_registered_account(testapp):
    """
    """
    account = {
        'email': 'please@work.com',
        'password': 'halo',
    }
    token = testapp.post('/api/v1/auth/login', json.dumps(account)).json['token']
    testapp.authorization = ('Bearer', token)

    response = testapp.get('/api/v1/passwords', json.dumps(account), status='2**')
    assert response.status_code == 200


def test_can_create_password_with_registered_account(testapp):
    """
    """
    account = {
        'email': 'please@work.com',
        'password': 'halo',
    }
    token = testapp.post('/api/v1/auth/login', json.dumps(account)).json['token']
    testapp.authorization = ('Bearer', token)

    passwords = {'website': 'www.google.com', 'login': 'test@test.com', 'password': 'test'}
    response = testapp.post('/api/v1/passwords', json.dumps(passwords), status='2**')
    assert response.status_code == 201


def test_fails_without_website_kwarg_for_registered_account(testapp):
    """
    """
    account = {
        'email': 'please@work.com',
        'password': 'halo',
    }
    token = testapp.post('/api/v1/auth/login', json.dumps(account)).json['token']
    testapp.authorization = ('Bearer', token)

    passwords = {'notwebsite': 'www.google.com', 'login': 'test@test.com', 'password': 'test'}
    response = testapp.post('/api/v1/passwords', json.dumps(passwords), status='4**')
    assert response.status_code == 400


def test_fails_without_login_kwarg_for_registered_account(testapp):
    """
    """
    account = {
        'email': 'please@work.com',
        'password': 'halo',
    }
    token = testapp.post('/api/v1/auth/login', json.dumps(account)).json['token']
    testapp.authorization = ('Bearer', token)

    passwords = {'website': 'www.google.com', 'notlogin': 'test@test.com', 'password': 'test'}
    response = testapp.post('/api/v1/passwords', json.dumps(passwords), status='4**')
    assert response.status_code == 400


def test_fails_without_password_kwarg_for_registered_account(testapp):
    """
    """
    account = {
        'email': 'please@work.com',
        'password': 'halo',
    }
    token = testapp.post('/api/v1/auth/login', json.dumps(account)).json['token']
    testapp.authorization = ('Bearer', token)

    passwords = {'website': 'www.google.com', 'login': 'test@test.com', 'notpassword': 'nottest'}
    response = testapp.post('/api/v1/passwords', json.dumps(passwords), status='4**')
    assert response.status_code == 400


def test_passes_when_listing_all_passwords_for_registered_account(testapp):
    """
    """
    account = {
        'email': 'please@work.com',
        'password': 'halo',
    }
    token = testapp.post('/api/v1/auth/login', json.dumps(account)).json['token']
    testapp.authorization = ('Bearer', token)

    passwords = {'website': 'www.notgoogle.com', 'login': 'test@test.com', 'password': 'test'}
    testapp.authorization = ('Bearer', token)
    testresponse = testapp.post('/api/v1/passwords', json.dumps(passwords), status='2**')
    print('this is test response', testresponse)
    request = testapp.get('/api/v1/passwords')
    assert request.status_code == 200
