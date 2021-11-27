import logging
import shlex
import subprocess

logger = logging.getLogger(__name__)

CLEAR_NETBOOT_BIN = "/usr/bin/beaker-clear-netboot"
CLEAR_NETBOOT_CMD = "sudo {bin} {{fqdn}}".format(bin=CLEAR_NETBOOT_BIN)


def clear_netboot(fqdn: str):
    """Remove netboot configuration for given FQDN."""

    logger.debug('clear_netboot %s', fqdn)

    fqdn_command = CLEAR_NETBOOT_CMD.format(fqdn=fqdn)
    full_command = shlex.split(fqdn_command)

    p = subprocess.Popen(full_command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    output, _ = p.communicate()

    if p.returncode:
        raise RuntimeError('sudo beaker-clear-netboot failed: %s' % output.strip())

    logger.debug('clear_netboot %s completed', fqdn)