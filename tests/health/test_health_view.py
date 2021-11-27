import http


def test_health_get(client):
    response = client.get(client.app.url_path_for("get_health"))
    payload = response.json()

    assert response.status_code == http.HTTPStatus.OK
    assert payload == "Healthy!"


def test_health_head(client):
    response = client.head(client.app.url_path_for("get_health"))

    assert response.status_code == http.HTTPStatus.OK
    assert not response.text
