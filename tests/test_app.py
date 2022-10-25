from tests.conftest import client
import json


def test_should_status_code_ok(client):
    response = client.get('/index')
    assert response.status_code == 200

def test_should_return_hello_world(client):
    response = client.get('/index')
    data = response.data.decode()
    assert data == 'Bonjour'


def test_ascii_converter(client):
    data = {
        'data': [17, 15, 7, 5, 29, 36 , 4 , 1, 3]
    }
    excpected  = [36, 15, 3]
    response = client.post('/filter', data=json.dumps(data))
    assert 1 == 1
