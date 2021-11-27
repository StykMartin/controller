import http
import unittest.mock


@unittest.mock.patch("controller.installation.service.clear_netboot")
def test_health_get_no_error(_, client):
    response = client.get(
        client.app.url_path_for("get_no_pxe", **{"fqdn": "test.fqdn"})
    )

    assert response.status_code == http.HTTPStatus.NO_CONTENT


@unittest.mock.patch("controller.installation.service.clear_netboot")
def test_health_get_error(mock, client):
    mock.side_effect = RuntimeError()

    response = client.get(
        client.app.url_path_for("get_no_pxe", **{"fqdn": "test.fqdn"})
    )

    # Let blame user for this failure
    assert response.status_code == http.HTTPStatus.BAD_REQUEST
