import http
import unittest.mock

import pytest

T_FQDN = "test.fqdn"
T_RECIPE_ID = 1


@unittest.mock.patch("controller.installation.service.clear_netboot")
def test_no_pxe_get(_, client):
    response = client.get(client.app.url_path_for("get_no_pxe", **{"fqdn": T_FQDN}))

    assert response.status_code == http.HTTPStatus.NO_CONTENT


@unittest.mock.patch("controller.installation.service.clear_netboot")
def test_no_pxe_get_failed_netboot_command(mock, client):
    mock.side_effect = RuntimeError()

    response = client.get(client.app.url_path_for("get_no_pxe", **{"fqdn": T_FQDN}))

    # Let blame user for this failure
    assert response.status_code == http.HTTPStatus.BAD_REQUEST


@pytest.mark.parametrize("t_fqdn", ["example*.com", "👀.com", "give me sudo"])
def test_no_pxe_get_user_error_fqdn(client, t_fqdn):
    response = client.get(client.app.url_path_for("get_no_pxe", **{"fqdn": t_fqdn}))

    # Let blame user for this failure
    assert response.status_code == http.HTTPStatus.BAD_REQUEST


@pytest.mark.parametrize(
    "method", ["get_install_start", "get_install_done", "get_post_install_done", "get_post_reboot", "get_install_fail"]
)
def test_install_get(client, method):
    response = client.get(client.app.url_path_for(method, **{"recipe_id": T_RECIPE_ID}))

    assert response.status_code == http.HTTPStatus.OK
    assert response.json() is True


def test_install_done_fqdn_get(client):
    """Make sure we can pass FQDN as additional parameter to install_done endpoint."""
    response = client.get(client.app.url_path_for("get_install_done", **{"recipe_id": T_RECIPE_ID, "fqdn": T_FQDN}))

    assert response.status_code == http.HTTPStatus.OK
    assert response.json() is True
