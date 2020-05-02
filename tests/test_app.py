class TestApp:
    def test_welcome(self, client):
        request = client.get('/')
        assert request.status_code == 200
        assert b'Welcome Home!' in request.data
