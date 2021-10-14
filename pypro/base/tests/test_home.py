from django.test.client import Client


def test_status_code(client: Client):
    resp = client.get('/')
    assert resp.status_code == 200
