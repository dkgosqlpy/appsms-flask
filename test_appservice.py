from appservice import appservice
with appservice.test_client() as c:
    response = c.get('/client')
    assert response.data == b'Hello World!'
    assert response.status_code == 200
