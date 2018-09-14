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
