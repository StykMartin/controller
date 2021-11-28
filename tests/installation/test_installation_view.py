import http
import unittest.mock

import pytest


@unittest.mock.patch("controller.installation.service.clear_netboot")
def test_health_get(_, client):
    response = client.get(client.app.url_path_for("get_no_pxe", **{"fqdn": "test.fqdn"}))

    assert response.status_code == http.HTTPStatus.NO_CONTENT


@unittest.mock.patch("controller.installation.service.clear_netboot")
def test_health_get_failed_netboot_command(mock, client):
    mock.side_effect = RuntimeError()

    response = client.get(client.app.url_path_for("get_no_pxe", **{"fqdn": "test.fqdn"}))

    # Let blame user for this failure
    assert response.status_code == http.HTTPStatus.BAD_REQUEST


@pytest.mark.parametrize("t_fqdn", ["example*.com", "👀.com", "give me sudo"])
def test_health_get_user_error_fqdn(client, t_fqdn):

    response = client.get(client.app.url_path_for("get_no_pxe", **{"fqdn": t_fqdn}))

    # Let blame user for this failure
    assert response.status_code == http.HTTPStatus.BAD_REQUEST
