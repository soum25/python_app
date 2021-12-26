from appli_file import application_main


def test_base_route():
    client = application_main.app.test_client()
    url = '/'

    response = client.get(url)
    assert response.get_data() == b'Hello World'
    assert response.status_code == 200
