import subprocess
import unittest.mock

import pytest


@unittest.mock.patch("subprocess.Popen")
def test_clear_netboot(popen_mock):
    from controller.installation.service import CLEAR_NETBOOT_CMD, clear_netboot

    popen_mock.return_value.communicate.return_value = "All good here", ""
    popen_mock.return_value.returncode = 0
    t_fqdn = "this.is.just.test.fqdn"

    clear_netboot(t_fqdn)

    popen_mock.assert_called()
    popen_mock.assert_called_once_with(
        CLEAR_NETBOOT_CMD.format(fqdn=t_fqdn).split(),
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    popen_mock.return_value.communicate.assert_called()


@unittest.mock.patch("subprocess.Popen")
def test_clear_netboot_error(popen_mock):
    from controller.installation.service import CLEAR_NETBOOT_CMD, clear_netboot

    t_output = "THIS IS BAD"
    popen_mock.return_value.communicate.return_value = t_output, ""
    popen_mock.return_value.returncode = 42
    t_fqdn = "this.is.just.test.fqdn"

    with pytest.raises(RuntimeError) as e:
        clear_netboot(t_fqdn)
        assert t_output in e

    popen_mock.assert_called()
    popen_mock.assert_called_once_with(
        CLEAR_NETBOOT_CMD.format(fqdn=t_fqdn).split(),
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    popen_mock.return_value.communicate.assert_called()
