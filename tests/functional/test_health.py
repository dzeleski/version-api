

def test_health(test_client):

    response = test_client.get('/health')
    assert 200 == response.status_code
